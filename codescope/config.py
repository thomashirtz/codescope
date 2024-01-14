from pathlib import Path
from typing import List, Optional

DELIMITER = "\n---\n"
EXCLUDED_DIRECTORIES = ["venv", "__pycache__"]


def is_hidden_directory(path: Path) -> bool:
    """
    Check if a directory is hidden.

    Args:
        path (Path): The Path object of the directory.

    Returns:
        bool: True if it's a hidden directory, False otherwise.
    """
    return any(part.startswith(".") and part != "." for part in path.parts)


def is_excluded_directory(path: Path, custom_exclusions: Optional[List[str]] = None) -> bool:
    """
    Check if a directory is in the excluded directories list or custom exclusions.

    Args:
        path (Path): The Path object of the directory.
        custom_exclusions (Optional[List[str]]): Custom directories to exclude.

    Returns:
        bool: True if it's an excluded directory, False otherwise.
    """
    if custom_exclusions is None:
        custom_exclusions = []
    exclusions = set(EXCLUDED_DIRECTORIES) | set(custom_exclusions)
    return any(part in exclusions for part in path.parts)


def should_exclude_directory(path: str, custom_exclusions: Optional[List[str]] = None) -> bool:
    """
    Determines whether a directory should be excluded from processing.

    Args:
        path (str): The path of the directory to be checked.
        custom_exclusions (Optional[List[str]]): Custom directories to exclude.

    Returns:
        bool: True if the directory should be excluded, False otherwise.
    """
    path_obj = Path(path)
    return is_hidden_directory(path_obj) or is_excluded_directory(path_obj, custom_exclusions)
