import ast
from pathlib import Path
from typing import Union

from codescope.config import should_exclude_directory


def extract_ast_item_summary(
        item: Union[ast.FunctionDef, ast.ClassDef],
        include_docstrings: bool,
        indent_level: int = 0
) -> str:
    """
    Extracts and formats a summary from an AST item, which can be a function or a class.

    Args:
        item (Union[ast.FunctionDef, ast.ClassDef]): The AST node representing a function or class.
        include_docstrings (bool): Whether to include docstrings in the summary.
        indent_level (int): The level of indentation for formatting the summary.

    Returns:
        str: The formatted summary of the given AST item.
    """
    indent = '  ' * indent_level
    item_type = 'Method' if indent_level > 0 else item.__class__.__name__.rstrip('Def')
    summary = f"{indent}{item_type}: `{item.name}`\n"

    if include_docstrings and (docstring := ast.get_docstring(item)):
        formatted_docstring = docstring.replace('\n', '\n' + indent + '    ').strip()
        summary += f"{indent}  Docstring: ```{formatted_docstring}```\n"

    if isinstance(item, ast.ClassDef):
        for class_item in item.body:
            if isinstance(class_item, ast.FunctionDef):
                summary += extract_ast_item_summary(class_item, include_docstrings, indent_level + 1)

    return summary


def extract_functions_and_classes(
        filepath: Path,
        include_docstring: bool
) -> str:
    """
    Extracts and summarizes functions and classes from a Python file.

    Args:
        filepath (Path): The path to the Python file.
        include_docstring (bool): Whether to include docstrings in the summary.

    Returns:
        str: The summary of functions and classes in the given file.
    """
    summary = "\n"

    try:
        with filepath.open('r') as file:
            node = ast.parse(file.read(), filename=str(filepath))

        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.ClassDef)):
                summary += extract_ast_item_summary(item, include_docstring) + '\n'
    except IOError as e:
        summary += f"Error reading file {filepath}: {e}\n"

    return summary


def extract_functions_classes_summary(
        path: Union[str, Path],
        include_docstrings: bool
) -> str:
    """
    Generates a summary of functions and classes for all Python files in the specified directory.

    Args:
        path (Union[str, Path]): The path to the directory to summarize.
        include_docstrings (bool): Whether to include docstrings in the summary.

    Returns:
        str: The comprehensive summary of all functions and classes in the directory.
    """
    summary = ""
    directory = Path(path)

    for file in directory.rglob('*.py'):
        if should_exclude_directory(str(file.parent)):
            continue
        summary += f"\nIn {file}:\n"
        summary += extract_functions_and_classes(file, include_docstring=include_docstrings)

    return summary
