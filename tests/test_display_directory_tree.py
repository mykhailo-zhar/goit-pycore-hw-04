"""Tests for scripts.display_directory_tree."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest
from colorama import Fore

from src.scripts.display_directory_tree import main

_ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m")


def strip_ansi(text: str) -> str:
    return _ANSI_ESCAPE.sub("", text)


def test_missing_argv(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py"])
    with pytest.raises(ValueError, match="Usage"):
        main()


def test_path_not_exists(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    missing = tmp_path / "nope"
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(missing)])
    with pytest.raises(FileNotFoundError):
        main()


def test_path_is_not_directory(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    path = tmp_path / "file.txt"
    path.write_text("x", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(path)])
    with pytest.raises(NotADirectoryError):
        main()


def test_empty_directory(monkeypatch: pytest.MonkeyPatch, capsys, tmp_path: Path):
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(tmp_path)])
    main()
    out = strip_ansi(capsys.readouterr().out)
    lines = [ln for ln in out.strip().splitlines() if ln.strip()]
    assert len(lines) == 1
    assert tmp_path.name in lines[0]


def test_directories_before_files(
    monkeypatch: pytest.MonkeyPatch, capsys, tmp_path: Path
):
    (tmp_path / "zzz.txt").write_text("z", encoding="utf-8")
    (tmp_path / "aaa").mkdir()
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(tmp_path)])
    main()
    out = strip_ansi(capsys.readouterr().out)
    idx_aaa = out.index("aaa")
    idx_zzz = out.index("zzz")
    assert idx_aaa < idx_zzz


def test_two_levels_expanded(monkeypatch: pytest.MonkeyPatch, capsys, tmp_path: Path):
    d = tmp_path / "outer"
    d.mkdir()
    (d / "inner.txt").write_text("i", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(tmp_path)])
    main()
    out = strip_ansi(capsys.readouterr().out)
    assert "outer" in out
    assert "inner.txt" in out


def test_third_level_directory_summarized_with_count(
    monkeypatch: pytest.MonkeyPatch, capsys, tmp_path: Path
):
    a = tmp_path / "a"
    b = a / "b"
    b.mkdir(parents=True)
    (b / "deep.txt").write_text("d", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(tmp_path)])
    main()
    out = strip_ansi(capsys.readouterr().out)
    assert "b (1 item)" in out


def test_third_level_empty_directory_summarized_zero(
    monkeypatch: pytest.MonkeyPatch, capsys, tmp_path: Path
):
    (tmp_path / "a" / "b").mkdir(parents=True)
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(tmp_path)])
    main()
    out = strip_ansi(capsys.readouterr().out)
    assert "b (0 items)" in out


def test_file_at_level_two_still_printed(
    monkeypatch: pytest.MonkeyPatch, capsys, tmp_path: Path
):
    d = tmp_path / "folder"
    d.mkdir()
    (d / "leaf.txt").write_text("x", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(tmp_path)])
    main()
    out = strip_ansi(capsys.readouterr().out)
    assert "leaf.txt" in out


def test_colors_present(monkeypatch: pytest.MonkeyPatch, capsys, tmp_path: Path):
    monkeypatch.setattr(sys, "argv", ["display_directory_tree.py", str(tmp_path)])
    (tmp_path / "file.txt").write_text("x", encoding="utf-8")
    (tmp_path / "folder").mkdir()
    main()
    out = capsys.readouterr().out
    assert Fore.CYAN in out
    assert Fore.GREEN in out
