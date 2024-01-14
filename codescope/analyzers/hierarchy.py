from pathlib import Path

from codescope.config import should_exclude_directory


def generate_file_hierarchy(path: str, indent_size: int = 4, include_files: bool = True) -> str:
    """
    Generates a visual tree structure of the file system starting from the specified path.

    This function traverses the directory tree starting from the given path, creating
    a string representation of the directory and file structure. It allows for configurable
    indentation and the option to include or exclude files in the output.

    Args:
        path (str): The root directory from which to start generating the tree structure.
        indent_size (int): The size of the indentation for each level of the tree (default is 4).
        include_files (bool): Flag to include files in the tree structure (default is True).

    Returns:
        str: A string representation of the tree structure of the file system.
    """
    root_path = Path(path)
    tree_structure = ""

    def add_directory_to_tree(directory: Path, level: int) -> None:
        """
        Recursively adds directories and (optionally) files to the tree structure.

        This inner function traverses the directory, adding each directory and file to the
        tree structure string with appropriate indentation based on its level in the directory
        tree.

        Args:
            directory (Path): The directory path currently being processed.
            level (int): The current level in the directory tree, used for indentation.
        """
        nonlocal tree_structure
        # Skip excluded directories
        if should_exclude_directory(str(directory)):
            return

        # Indent the directory name based on its level
        indent = " " * indent_size * level
        tree_structure += f"{indent}{directory.name}/\n"

        # Iterate over items in the directory
        for item in directory.iterdir():
            # Add subdirectories
            if item.is_dir():
                add_directory_to_tree(item, level + 1)
            # Add files if include_files is True
            elif include_files and item.is_file():
                tree_structure += f"{indent}{' ' * indent_size}{item.name}\n"

    # Start building the tree from the root path
    add_directory_to_tree(root_path, level=0)
    return tree_structure
