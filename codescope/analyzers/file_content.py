from pathlib import Path
from typing import Union

from codescope.config import should_exclude_directory


def extract_file_contents(path: Union[str, Path]) -> str:
    """
    Generates a summary of the contents of all Python files in the specified directory.

    Args:
        path (Union[str, Path]): The path to the directory to summarize.

    Returns:
        str: A comprehensive summary of the contents of all Python files in the directory.
    """
    summary = "Each file's content is presented below, delimited by three `.\n\n"
    directory = Path(path)

    for file in directory.rglob("*.py"):
        if should_exclude_directory(str(file.parent)):
            continue
        summary += f"\nIn {file}:\n```\n"
        try:
            with file.open("r", errors="ignore") as file_content:
                summary += file_content.read()
        except IOError as e:
            summary += f"Error reading file {file}: {e}"
        summary += "```\n\n"

    return summary
