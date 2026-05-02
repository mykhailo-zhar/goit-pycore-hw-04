import pytest

from src.salary import total_salary
from tests.helpers import resolve_path


def get_total_salary(path: str) -> tuple[int, int]:
    """
    Get the total salary of the employees in the given file.

    Args:
        path (str): The path to the file containing the employee data.

    Returns:
        tuple[int, int]: A tuple containing the total salary and its average.
    """
    return total_salary(resolve_path(path))


def test_total_salary_signature():

    result = get_total_salary("salary/salary-sample")

    assert (
        isinstance(result, tuple)
        and len(result) == 2
        and all(isinstance(x, int) for x in result)
    )


def test_empty_file():
    result = get_total_salary("salary/salary-empty")
    assert result == (0, 0)


def test_non_existent_file():
    with pytest.raises(FileNotFoundError):
        get_total_salary("salary/salary-non-existent")


def test_writeonly_file(writeonly_file):
    with pytest.raises(PermissionError):
        total_salary(writeonly_file)


def test_corrupted_file_with_empty_line():
    with pytest.raises(ValueError):
        get_total_salary("salary/salary-corrupted-empty-line")


def test_corrupted_file_with_invalid_salary():
    with pytest.raises(ValueError):
        get_total_salary("salary/salary-corrupted-invalid-salary")


def test_corrupted_file_with_invalid_name():
    with pytest.raises(ValueError):
        get_total_salary("salary/salary-corrupted-invalid-name")


def test_corrupted_file_with_no_comma():
    with pytest.raises(ValueError):
        get_total_salary("salary/salary-corrupted-no-comma")


def test_sample_file():
    result = get_total_salary("salary/salary-sample")
    assert result == (6000, 2000)


def test_sample_with_float_average():
    result = get_total_salary("salary/salary-sample-float-average")
    assert result == (5000, 1667)
