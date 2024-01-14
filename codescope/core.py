from codescope.analyzers.code_structure import summarize_project_code
from codescope.analyzers.file_content import extract_file_contents
from codescope.analyzers.hierarchy import generate_file_hierarchy
from codescope.analyzers.readme import get_readme_content
from codescope.config import DELIMITER


def compile_project_summary(
    project_path: str,
    include_tree: bool,
    include_inspection: bool,
    include_readme: bool,
    include_docstrings: bool,
    include_full_file_content: bool,
    include_context_prompt: bool = True,
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
        summary += "\nProject Structure:\n" + generate_file_hierarchy(project_path)
        summary += DELIMITER

    if include_inspection:
        summary += "\nKey Functions and Classes:\n"
        summary += summarize_project_code(project_path, include_docstrings)
        summary += DELIMITER

    if include_full_file_content:
        summary += "\nFile Content:\n"
        summary += extract_file_contents(project_path)
        summary += DELIMITER

    return summary
