# -*- coding: utf-8 -*-
"""界面多语言（i18n）测试：越南语词典完整性、越南记法、越南语界面文字。"""
import ast
import pathlib
import string

import pytest

import i18n
from i18n import tr
from i18n.vi import MESSAGES

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = (sorted((ROOT / "gui").glob("*.py")) + sorted((ROOT / "core").glob("*.py"))
           + sorted((ROOT / "engine").glob("*.py"))
           + sorted((ROOT / "recognition").glob("*.py")) + [ROOT / "main.py"])


@pytest.fixture
def vi():
    i18n.set_language("vi")
    yield
    i18n.set_language("zh")


def _placeholders(text: str) -> set:
    return {field for _lit, field, _spec, _conv in string.Formatter().parse(text)
            if field is not None}


def _literal_tr_keys():
    keys = {}
    for path in SOURCES:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == "tr" and node.args
                    and isinstance(node.args[0], ast.Constant)
                    and isinstance(node.args[0].value, str)):
                keys.setdefault(node.args[0].value, f"{path.name}:{node.lineno}")
    return keys


# ---------------------------------------------------------------- 词典完整性
def test_every_literal_tr_key_has_vietnamese():
    keys = _literal_tr_keys()
    assert len(keys) > 100
    missing = {k: where for k, where in keys.items() if k not in MESSAGES}
    assert not missing, f"越南语词典缺少: {missing}"


def test_placeholders_match():
    bad = {k: v for k, v in MESSAGES.items() if _placeholders(k) != _placeholders(v)}
    assert not bad, f"占位符不一致: {bad}"


def test_dynamic_keys_have_vietnamese():
    from core.board import PIECE_NAMES
    from core.openings import opening_names
    from gui.import_dialog import _CORNER_NAMES
    from gui.main_window import TAKEOVER_BUTTON_TEXT
    dynamic = (set(PIECE_NAMES.values()) | {n for n in opening_names() if n}
               | set(_CORNER_NAMES) | {TAKEOVER_BUTTON_TEXT}
               | {"红方", "黑方", "红", "黑", "长将", "长捉", "一将一捉",
                  "绝杀", "困毙", "将军", "中模型", "小模型", "万能带旋转",
                  "极快（不模拟轨迹，直接两次点击）", "快", "中", "慢"})
    missing = sorted(k for k in dynamic if k not in MESSAGES)
    assert not missing, f"越南语词典缺少: {missing}"


def test_translations_have_no_chinese_except_board_glyphs():
    """译文不应残留汉字（棋子字形除外，例如摆子面板的棋子按钮）。"""
    leaked = {k: v for k, v in MESSAGES.items()
              if any("\u4e00" <= ch <= "\u9fff" for ch in v)}
    assert not leaked, f"译文含中文: {leaked}"


# ---------------------------------------------------------------- 语言切换
def test_default_language_is_vietnamese():
    assert i18n.DEFAULT_LANGUAGE == "vi"
    from gui.main_window import DEFAULT_CONFIG
    assert DEFAULT_CONFIG["language"] == "vi"


def test_set_language_fallback_and_zh_passthrough():
    i18n.set_language("xx")
    assert i18n.get_language() == i18n.DEFAULT_LANGUAGE
    i18n.set_language("zh")
    assert tr("双方均势") == "双方均势"
    assert tr("{who}领先 {lead:.2f}", who="红方", lead=1.5) == "红方领先 1.50"


def test_missing_key_falls_back_to_source(vi):
    assert tr("这条不在词典里") == "这条不在词典里"


# ---------------------------------------------------------------- 越南记法
@pytest.mark.parametrize("iccs, expected", [
    ("h2e2", "P2-5"), ("h0g2", "M2.3"), ("b0c2", "M8.7"), ("c3c4", "B7.1"),
    ("i0i1", "X1.1"), ("g0e2", "T3.5"), ("f0e1", "S4.5"), ("e0e1", "Tg5.1"),
])
def test_vietnamese_notation_red(iccs, expected):
    from core.board import Board, iccs_to_move, move_to_vietnamese
    assert move_to_vietnamese(Board(), iccs_to_move(iccs)) == expected


def test_vietnamese_notation_black():
    from core.board import Board, iccs_to_move, move_to_vietnamese
    b = Board()
    b.make_move(iccs_to_move("h2e2"))
    assert move_to_vietnamese(b, iccs_to_move("h7e7")) == "P8-5"
    assert move_to_vietnamese(b, iccs_to_move("b9c7")) == "M2.3"


def test_vietnamese_notation_tandem_and_retreat():
    from core.board import Board, move_to_vietnamese
    b = Board("9/9/9/9/9/9/9/9/R8/R3K4 w - - 0 1")
    assert move_to_vietnamese(b, ((8, 0), (8, 5))) == "Xt-4"
    assert move_to_vietnamese(b, ((9, 0), (9, 5))) == "Xs-4"
    assert move_to_vietnamese(b, ((8, 0), (5, 0))) == "Xt.3"
    b2 = Board("4k4/9/9/9/9/9/R8/9/9/4K4 w - - 0 1")
    assert move_to_vietnamese(b2, ((6, 0), (8, 0))) == "X9/2"


def test_move_text_follows_language(vi):
    from core.board import Board, iccs_to_move, move_to_text
    assert move_to_text(Board(), iccs_to_move("h2e2")) == "P2-5"
    i18n.set_language("zh")
    assert move_to_text(Board(), iccs_to_move("h2e2")) == "炮二平五"


def test_game_move_list_in_vietnamese(vi):
    from core.board import iccs_to_move
    from core.game import Game
    g = Game()
    g.play(iccs_to_move("h2e2"))
    g.play(iccs_to_move("h7e7"))
    assert g.move_list_text() == ["P2-5", "P8-5"]


# ---------------------------------------------------------------- 越南语界面文字
def test_board_messages_in_vietnamese(vi):
    from core.board import Board
    over, msg = Board("R2k5/R8/9/9/9/9/9/9/9/4K4 b - - 0 1").is_game_over()
    assert over and msg == "Đỏ thắng (Đen bị chiếu bí)"
    err = Board("rr1k1r3/9/9/9/9/9/9/9/9/4K4 w - - 0 1").validate_position()
    assert err == "Đen: Xe vượt quá 2 quân (hiện có 3)"


def test_opening_label_in_vietnamese(vi):
    from core.openings import opening_label, opening_names
    assert opening_label("") == "Mặc định (engine chọn nước tốt nhất)"
    labels = [opening_label(n) for n in opening_names() if n]
    assert labels and all(not any("\u4e00" <= ch <= "\u9fff" for ch in s)
                          for s in labels)


def test_engine_panel_in_vietnamese(qapp, vi):
    from gui.engine_panel import EnginePanel
    p = EnginePanel()
    assert p._fmt_lead(0.5) == "Hai bên cân bằng"
    assert p._fmt_lead(150) == "Đỏ dẫn trước 1.50"
    p.set_stm("w")
    assert "Đến lượt" in p.turn_label.text()


def test_main_window_builds_in_vietnamese(qapp, vi):
    """越南语下主窗口可正常构建，且主要按钮文字已翻译。"""
    from PyQt6.QtWidgets import QAbstractButton
    from gui.main_window import MainWindow
    w = MainWindow()
    try:
        texts = [b.text() for b in w.findChildren(QAbstractButton) if b.text()]
        assert texts
        leaked = [t for t in texts if any("\u4e00" <= ch <= "\u9fff" for ch in t)]
        assert not leaked, f"按钮文字仍为中文: {leaked}"
    finally:
        w.close()
