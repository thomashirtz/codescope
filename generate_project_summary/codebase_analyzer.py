from typing import Optional
from pathlib import Path
from clipboard import copy

from generate_project_summary.code_structure_extractor import extract_functions_classes_summary
from generate_project_summary.file_tree_generator import generate_file_tree
from generate_project_summary.config import DELIMITER


def generate_codebase_summary(
        project_path: str,
        include_tree: bool,
        include_inspection: bool,
        include_readme: bool,
        include_docstrings: bool,
        output_filepath: Optional[str] = None,
        include_context_prompt: bool = True,
        clipboard: bool = False,
) -> None:
    """
    Generates a comprehensive summary of a Python project located at the specified path.

    This function aggregates various components of the project, such as the README file,
    file tree structure, and a summary of functions and classes. The result can be written
    to a file, copied to the clipboard, or printed to the console.

    Args:
        project_path (str): The root directory of the Python project.
        include_tree (bool): Whether to include the project's file tree structure.
        include_inspection (bool): Whether to include a summary of functions and classes.
        include_readme (bool): Whether to include the README content.
        include_docstrings (bool): Whether to include docstrings in the function and class summary.
        output_filepath (Optional[str]): Path to the file where the summary will be saved. If None, prints to the console.
        include_context_prompt (bool): Whether to include a context prompt at the beginning of the summary.
        clipboard (bool): Whether to copy the summary to the clipboard.
    """
    summary = compile_project_summary(
        project_path=project_path,
        include_tree=include_tree,
        include_inspection=include_inspection,
        include_readme=include_readme,
        include_docstrings=include_docstrings,
        include_context_prompt=include_context_prompt
    )
    output_summary(
        summary=summary,
        output_filepath=output_filepath,
        clipboard=clipboard
    )


def compile_project_summary(
        project_path: str,
        include_tree: bool,
        include_inspection: bool,
        include_readme: bool,
        include_docstrings: bool,
        include_context_prompt: bool
) -> str:
    """
    Compiles and returns a comprehensive summary of the specified Python project.

    This function aggregates different components of the project into a single summary string.
    It can include the project's README content, a file tree structure, and a detailed summary
    of the project's functions and classes. Each component is included based on the corresponding
    boolean flags provided. The function allows customization of the summary content based on
    the specified parameters.

    Args:
        project_path (str): The file path to the root of the project directory.
        include_tree (bool): If True, includes the project's file tree structure in the summary.
        include_inspection (bool): If True, adds a summary of functions and classes in the project.
        include_readme (bool): If True, incorporates the content of the project's README.md file.
        include_docstrings (bool): If set and include_inspection is True, includes docstrings
                                   in the functions and classes summary.
        include_context_prompt (bool): If True, begins the summary with a context prompt line.

    Returns:
        str: A string containing the compiled summary of the project based on the specified components.
    """

    if include_context_prompt:
        summary = "The following information provides context for a Python project codebase. Future questions will be related to this specific codebase. Please focus on this context for any subsequent inquiries and avoid generating responses outside this specified context. Please ask for clarifications or additional details as needed.\n" + DELIMITER
    else:
        summary = ""

    if include_readme:
        summary += "\nProject Overview:\n" + get_readme_content(project_path)

    if include_tree:
        summary += DELIMITER + "\nFile Tree Structure:\n" + generate_file_tree(project_path)

    if include_inspection:
        summary += DELIMITER + "\nKey Functions and Classes:\n"
        summary += extract_functions_classes_summary(project_path, include_docstrings)

    return summary


def get_readme_content(project_path: str) -> str:
    """
    Reads and returns the content of the README.md file located in the specified project path.

    This function attempts to open and read the README.md file in the given project directory.
    If the README.md file does not exist at the location, it returns a default message
    indicating that the file could not be found.

    Args:
        project_path (str): The file path to the root of the project directory
                            where README.md is expected to be located.

    Returns:
        str: The content of the README.md file as a string. If the file is not found,
             it returns a message indicating that no README.md was found.

    Raises:
        FileNotFoundError: If the README.md file does not exist in the specified path.
                           This exception is caught and handled internally.
    """
    readme_path = Path(project_path) / 'README.md'
    try:
        return readme_path.read_text()
    except FileNotFoundError:
        return "No README.md found.\n"


def output_summary(
        summary: str,
        output_filepath: Optional[str],
        clipboard: bool
) -> None:
    """
    Outputs the generated project summary to one or more destinations.

    This function can output the summary in three ways: by writing it to a specified file,
    copying it to the clipboard, or printing it to the console. If a file path is provided,
    it writes the summary to that file. If the clipboard flag is set, it copies the summary
    to the system clipboard. If no file path is provided, it defaults to printing the summary
    to the console. In case of a file writing error, it catches and prints the error message.

    Args:
        summary (str): The project summary to be output.
        output_filepath (Optional[str]): The file path where the summary should be written.
                                         If None, the summary is printed to the console.
        clipboard (bool): If True, the summary is also copied to the clipboard.

    Raises:
        IOError: If an error occurs while writing the summary to a file.
    """
    if clipboard:
        copy(summary)
        print("Summary copied to clipboard.")

    if output_filepath:
        try:
            Path(output_filepath).write_text(summary)
            print(f"Summary written to {output_filepath}")
        except IOError as e:
            print(f"Error writing summary to file: {e}")
    else:
        print(summary)
