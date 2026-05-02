import re

from src.validations import validate_name, validate_positive_integer


def validate_line(line: str) -> tuple[str, str, str]:
    """
    Validate a line of cat data.
    """
    id, name, age = line.strip().split(",")

    if not re.match(r"^[a-f0-9]{24}$", id):
        raise ValueError(f"Invalid id: {id}")
    if not validate_name(name):
        raise ValueError(f"Invalid name: {name}")
    if not validate_positive_integer(str(age)):
        raise ValueError(f"Invalid age: {age}")

    return id, name, age


def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Get the information about the cats from the file.

    Args:
        path (str): The path to the file containing the cat data.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing the cat data.
    """
    with open(path, "r") as file:
        cats: list[dict[str, str]] = []
        for line in file:
            id, name, age = validate_line(line)
            cats.append(
                {
                    "id": id,
                    "name": name,
                    "age": str(age),
                }
            )
    return cats


def demo(path: str = "data/cats_file.txt"):
    """
    Demo function for the cats module.
    """
    cats = get_cats_info(path)
    print(cats)


if __name__ == "__main__":
    demo()
