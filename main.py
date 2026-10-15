# -*- coding: utf-8 -*-
"""象棋接管助手入口。

用法：
    .venv/Scripts/python main.py
"""
import os
import sys
import traceback


def _install_excepthook():
    """全局异常兜底：把未捕获异常写日志并弹框，而不是让进程直接消失。

    PyQt 中槽函数里的未捕获异常默认会让整个进程 abort（用户看到的就是
    "闪退"），这里接管后至少能留下可读的错误信息与日志。
    """
    log_path = os.path.join(os.path.expanduser("~"), "xq_assistant_error.log")

    def hook(exc_type, exc, tb):
        text = "".join(traceback.format_exception(exc_type, exc, tb))
        sys.stderr.write(text)
        try:
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(text + "\n" + "-" * 60 + "\n")
        except Exception:
            pass
        try:
            from PyQt6.QtWidgets import QApplication, QMessageBox
            from i18n import tr
            if QApplication.instance() is not None:
                QMessageBox.critical(
                    None, tr("出错了"),
                    tr("发生未预期的错误，操作未完成：\n\n{error}\n\n详细信息已写入：\n{log}",
                       error=f"{exc_type.__name__}: {exc}", log=log_path))
        except Exception:
            pass

    sys.excepthook = hook


_install_excepthook()

from PyQt6.QtCore import QLibraryInfo, QLocale, QTranslator  # noqa: E402
from PyQt6.QtWidgets import QApplication  # noqa: E402

from i18n import (DEFAULT_LANGUAGE, get_language, set_language, tr,  # noqa: E402
                  ui_font_family)
from gui.main_window import MainWindow, read_config  # noqa: E402


def _install_qt_translator(app: QApplication) -> None:
    """Qt 自带控件（OK/Cancel 等标准按钮、文件对话框）的翻译。"""
    translator = QTranslator(app)
    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    if translator.load(QLocale(get_language()), "qtbase", "_", path):
        app.installTranslator(translator)


def main():
    set_language(read_config().get("language", DEFAULT_LANGUAGE))
    app = QApplication(sys.argv)
    _install_qt_translator(app)
    if get_language() != "zh":
        # 系统默认字体若是中文字体（中文版 Windows），越南语声调符号会错位
        font = app.font()
        font.setFamily(ui_font_family())
        app.setFont(font)
    app.setApplicationName(tr("象棋接管助手"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
