# -*- coding: utf-8 -*-
"""界面多语言（i18n）。

以中文原文作为消息键（类似 gettext）：界面文字一律写成
``tr("中文原文", 参数=值)``。中文直接返回原文；其它语言查对应词典，
词典缺词时回退为中文原文，保证界面永远有字可显示。

带参数的文字用 ``str.format`` 命名占位符，例如
``tr("{who}领先 {lead:.2f}", who=..., lead=...)``——译文可以自由调整语序。
"""
from __future__ import annotations

from typing import Dict

from i18n.vi import MESSAGES as _VI_MESSAGES

DEFAULT_LANGUAGE = "vi"
# 语言代码 -> 该语言自己的名称（设置界面下拉框显示用）
LANGUAGES: Dict[str, str] = {"vi": "Tiếng Việt", "zh": "中文"}

_CATALOGS: Dict[str, Dict[str, str]] = {"zh": {}, "vi": _VI_MESSAGES}
_language = DEFAULT_LANGUAGE


def set_language(lang: str) -> None:
    """切换界面语言；未知语言代码回退为默认语言。"""
    global _language
    _language = lang if lang in LANGUAGES else DEFAULT_LANGUAGE


def get_language() -> str:
    return _language


def catalog(lang: str) -> Dict[str, str]:
    return _CATALOGS.get(lang, {})


def tr(text: str, **kwargs) -> str:
    """翻译界面文字（text 为中文原文）。"""
    msg = _CATALOGS.get(_language, {}).get(text, text)
    return msg.format(**kwargs) if kwargs else msg


def ui_font_family() -> str:
    """界面文字（非棋子）用的字体：中文用雅黑，越南文用含越南语变音的 Segoe UI。"""
    return "Microsoft YaHei" if _language == "zh" else "Segoe UI"
