import sys
from pathlib import Path

from colorama import Fore

TABULATIOM_SYMBOL = " " * 4


def validate_directory(path: str) -> Path:
    """
    Validate the directory.

    Args:
        path (str): The path to the directory to validate.

    Raises:
        FileNotFoundError: If the path does not exist.
        NotADirectoryError: If the path is not a directory.

    Returns:
        Path: The validated path.
    """
    resulting_path = Path(path)
    if not resulting_path.exists():
        raise FileNotFoundError(f"The path {path} does not exist")
    if not resulting_path.is_dir():
        raise NotADirectoryError(f"The path {path} is not a directory")
    return resulting_path


def print_directories(path: Path, level: int = 0, limit: int = 2):
    """
    Print the directories. Recursively.

    Terminal directories are to be printed when level is out of limit.
    Otherwise, the directory is printed as a normal directory.

    Under that directory, subdirectories are printed first
    And then files.

    Args:
        path (Path): The path to the directory to print.
        level (int, optional): The level of the directory to print. Defaults to 0.
        limit (int, optional): The limit of the directories to print. Defaults to 2.
    """
    if level == limit:
        print_terminal_directory(path, level)
        return

    print_directory(path, level)
    directories = sorted([file for file in path.iterdir() if file.is_dir()])
    for directory in directories:
        print_directories(directory, level + 1, limit)
    print_files(path, level + 1)


def print_terminal_directory(path: Path, level: int = 0):
    """
    Print a terminal directory.

    Terminal directory is a directory with a summary of its items.

    Items are counted as all objects under the directory.

    Directories are printed in alphabetical order.

    Args:
        path (Path): The path to the directory to print.
        level (int, optional): The level of the directory to print. Defaults to 0.
    """
    item_count = len([file for file in path.iterdir()])
    item_plural = "items" if abs(item_count) != 1 else "item"
    print(
        f"{TABULATIOM_SYMBOL * level}{Fore.CYAN}{path.name} ({item_count} {item_plural}){Fore.RESET}"
    )


def print_directory(path: Path, level: int = 0):
    """
    Print a normal directory.

    Args:
        path (Path): The path to the directory to print.
        level (int, optional): The level of the directory to print. Defaults to 0.
    """
    print(f"{TABULATIOM_SYMBOL * level}{Fore.CYAN}{path.name}/{Fore.RESET}")


def print_files(path: Path, level: int = 0):
    """
    Print the files under a directory.

    Files are printed in alphabetical order.

    Args:
        path (Path): The path to the directory to print.
        level (int, optional): The level of the directory to print. Defaults to 0.
    """
    files = sorted([file for file in path.iterdir() if file.is_file()])
    for file in files:
        print(f"{TABULATIOM_SYMBOL * (level)}{Fore.GREEN}{file.name}{Fore.RESET}")


def main():
    """
    Main function.

    It validates the directory and prints the directory tree.

    Raises:
        ValueError: If the usage is incorrect.
    """
    if len(sys.argv) < 2:
        raise ValueError("Usage: display_directory_tree.py <directory>")
    path = validate_directory(sys.argv[1])

    print_directories(path.absolute(), limit=2)


if __name__ == "__main__":
    main()
