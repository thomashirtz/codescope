from typing import Optional
from pathlib import Path
from clipboard import copy

from codescope.code_content_extractor import generate_file_contents_summary
from codescope.code_structure_extractor import extract_functions_classes_summary
from codescope.file_tree_generator import generate_file_tree
from codescope.config import DELIMITER


def generate_codebase_summary(
        project_path: str,
        include_tree: bool,
        include_inspection: bool,
        include_readme: bool,
        include_docstrings: bool,
        include_full_file_content: bool,
        output_filepath: Optional[str] = None,
        include_context_prompt: bool = True,
        clipboard: bool = False,
) -> None:
    """
    Generates and outputs a comprehensive summary of a Python project at the given path.

    This function consolidates various components like README content, file tree structure,
    and summaries of functions and classes. It allows selective inclusion of these components
    and outputs the summary to either a file, clipboard, or console.

    Args:
        project_path (str): The directory path of the Python project to summarize.
        include_tree (bool): Include file tree structure in the summary if True.
        include_inspection (bool): Include a summary of functions and classes if True.
        include_readme (bool): Include the content of README.md in the summary if True.
        include_docstrings (bool): Include docstrings in the functions and classes summary. Effective only if include_inspection is True.
        include_full_file_content (bool): Include the full content of Python files in the summary.
        output_filepath (Optional[str]): File path to save the summary. If None, prints to the console.
        include_context_prompt (bool): Start the summary with a context prompt if True.
        clipboard (bool): Copy the summary to the clipboard if True.

    Returns:
        None: This function does not return anything. It outputs the summary as specified.
    """
    summary = compile_project_summary(
        project_path=project_path,
        include_tree=include_tree,
        include_inspection=include_inspection,
        include_readme=include_readme,
        include_docstrings=include_docstrings,
        include_context_prompt=include_context_prompt,
        include_full_file_content=include_full_file_content,
    )
    output_summary(
        summary=summary,
        output_filepath=output_filepath,
        clipboard=clipboard,
    )


def compile_project_summary(
        project_path: str,
        include_tree: bool,
        include_inspection: bool,
        include_readme: bool,
        include_docstrings: bool,
        include_context_prompt: bool,
        include_full_file_content: bool = True,
) -> str:
    """
    Compiles a detailed summary of a Python project from various components.

    This function creates a unified summary string from selected components of a project,
    such as README.md content, file tree, and summaries of functions and classes.
    The inclusion of each component is controlled by boolean flags.

    Args:
        project_path (str): Path to the root of the project directory.
        include_tree (bool): Include file tree structure in the summary if True.
        include_inspection (bool): Include a summary of functions and classes if True.
        include_readme (bool): Include README.md content if True.
        include_docstrings (bool): Include docstrings in the summary of functions and classes if True. Relevant only if include_inspection is True.
        include_context_prompt (bool): Include a context prompt at the beginning of the summary if True.
        include_full_file_content (bool): Include full file contents in the summary if True.

    Returns:
        str: A string containing the compiled project summary.
    """

    if include_context_prompt:
        summary = "The following information provides context for a Python project codebase. Future questions will be related to this specific codebase. Please focus on this context for any subsequent inquiries and avoid generating responses outside this specified context. Please ask for clarifications or additional details as needed.\n"
        summary += "Please write a short Summary of this project so that it is easier for you to understand and answer the future questions.\n"
        summary += DELIMITER
    else:
        summary = ""

    if include_readme:
        summary += "\nREADME.md content:\n" + get_readme_content(project_path)
        summary += DELIMITER

    if include_tree:
        summary += "\nProject Structure:\n" + generate_file_tree(project_path)
        summary += DELIMITER

    if include_inspection:
        summary += "\nKey Functions and Classes:\n"
        summary += extract_functions_classes_summary(project_path, include_docstrings)
        summary += DELIMITER

    if include_full_file_content:
        summary += "\nFile Content:\n"
        summary += generate_file_contents_summary(project_path)
        summary += DELIMITER

    return summary


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
    Outputs the given project summary to a file, clipboard, or console.

    This function supports multiple modes of output for the project summary. It can write the summary
    to a specified file path, copy it to the clipboard, or print it to the console, based on the provided arguments.

    Args:
        summary (str): The project summary to be output.
        output_filepath (Optional[str]): The file path where the summary is to be written. If None, prints to the console.
        clipboard (bool): If True, the summary is also copied to the clipboard.

    Raises:
        IOError: Raised if there's an error writing the summary to the specified file, but handled internally.
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
