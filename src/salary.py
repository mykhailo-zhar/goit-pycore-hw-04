import re


def validate_line(line: str) -> tuple[str, int]:
    """
    Validate a line of employee data.

    Args:
        line (str): A string containing the employee data.

    Raises:
        ValueError: If the name is invalid.
        ValueError: If the salary is invalid.

    Returns:
        tuple[str, int]: A tuple containing the name and salary.
    """
    name, salary = line.split(",")
    # Checks whether the name consists of letters, spaces and digits
    if not re.match(r"^[\w\s0-9]+$", name):
        raise ValueError(f"Invalid name: {name}")

    # Checks whether the salary is a positive integer
    if not re.match(r"^\d+$", salary):
        raise ValueError(f"Invalid salary: {salary}")

    return name, int(salary)


def total_salary(path: str) -> tuple[int, int]:
    """
    Calculate the total salary of the employees in the given file.

    Args:
        path (str): The path to the file containing the employee data.

    Returns:
        tuple[int, int]: A tuple containing the total salary and its average.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file is not readable.
        ValueError: If the file is corrupted.
    """

    with open(path, "r") as file:
        total_salary: int = 0
        count: int = 0

        for line in file:
            _, salary = validate_line(line)
            total_salary += salary
            count += 1

    return (
        total_salary,
        int(round(total_salary / count, 0)) if count > 0 else 0,
    )


def demo(path: str = "data/salary_file.txt"):
    """
    Demo function for the salary module.

    Args:
        path (str, optional): The path to the salary file. Defaults to "data/salary_file.txt".
    """
    total, average = total_salary(path)
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )


if __name__ == "__main__":
    demo()
