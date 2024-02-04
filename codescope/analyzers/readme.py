from pathlib import Path


def get_readme_content(project_path: str) -> str:
    """
    Retrieves the content of the README.md file from the specified project path.

    Attempts to read and return the contents of README.md located in the project directory.
    If the file does not exist, a default message indicating its absence is returned.

    Args:
        project_path (str): The path to the project directory containing README.md.

    Returns:
        str: The content of README.md, or a message if the file is not found.

    Raises:
        FileNotFoundError: Raised if README.md does not exist at the specified path, but handled internally.
    """
    readme_path = Path(project_path) / "README.md"
    try:
        return readme_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return "No README.md found.\n"
