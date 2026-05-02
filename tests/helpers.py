from pathlib import Path


def resolve_path(path: str) -> str:
    """
    Resolve the path to the data file.

    Args:
        path (str): The path to the data file.

    Returns:
        str: The resolved path to the data file.
    """
    return str(Path(__file__).resolve().parent / "data" / path)
