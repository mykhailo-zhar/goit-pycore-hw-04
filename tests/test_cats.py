"""
Contract for ``get_cats_info`` exercised by these tests:

- Each non-empty line: ``<id>,<name>,<age>`` (split on comma with maxsplit 2).
- ``id``: ASCII letters and digits only (``^[a-zA-Z0-9]+$``).
- ``name``: same validation as ``src.validations.validate_name`` (Unicode word chars and whitespace).
- ``age``: decimal integer string; parsed value must be strictly greater than 0.
"""

import pytest

from src.cats import get_cats_info
from tests.helpers import resolve_path


def read_cats(path: str) -> list[dict[str, str]]:
    """
    Load cat records from a test fixture path under tests/data.

    Args:
        path (str): Relative path under tests/data (e.g. ``cats/cats-sample``).

    Returns:
        list[dict[str, str]]: One dict per cat with keys id, name, age (all str).
    """
    return get_cats_info(resolve_path(path))


def test_get_cats_info_signature():
    result = read_cats("cats/cats-sample")

    assert isinstance(result, list)
    assert len(result) == 5
    for item in result:
        assert isinstance(item, dict)
        assert set(item.keys()) == {"id", "name", "age"}
        assert all(isinstance(value, str) for value in item.values())


def test_empty_file():
    result = read_cats("cats/cats-empty")
    assert result == []


def test_non_existent_file():
    with pytest.raises(FileNotFoundError):
        read_cats("cats/cats-non-existent")


def test_writeonly_file(writeonly_file):
    with pytest.raises(PermissionError):
        get_cats_info(writeonly_file)


def test_corrupted_file_with_empty_line():
    with pytest.raises(ValueError):
        read_cats("cats/cats-corrupted-empty-line")


def test_corrupted_file_with_invalid_age():
    with pytest.raises(ValueError):
        read_cats("cats/cats-corrupted-invalid-age")


def test_corrupted_file_with_non_positive_age():
    with pytest.raises(ValueError):
        read_cats("cats/cats-corrupted-non-positive-age")


def test_corrupted_file_with_invalid_name():
    with pytest.raises(ValueError):
        read_cats("cats/cats-corrupted-invalid-name")


def test_corrupted_file_with_invalid_id():
    with pytest.raises(ValueError):
        read_cats("cats/cats-corrupted-invalid-id")


def test_corrupted_file_with_no_comma():
    with pytest.raises(ValueError):
        read_cats("cats/cats-corrupted-no-comma")


def test_corrupted_file_with_wrong_field_count():
    with pytest.raises(ValueError):
        read_cats("cats/cats-corrupted-wrong-count")


def test_sample_file():
    result = read_cats("cats/cats-sample")
    assert result == [
        {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
        {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
        {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
        {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
    ]
