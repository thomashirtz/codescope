import argparse

from codescope.core import compile_project_summary
from codescope.utilities import export_summary


def main() -> None:
    """
    Entry point for the command line interface to generate a comprehensive summary of a Python project.

    This function parses command line arguments to configure the generation of a project summary.
    It allows specification of the project path, output options, and various aspects of the project
    to include in the summary. The summary can be customized to include the project's file tree,
    README content, inspection of functions and classes, and their docstrings. There's also an option
    to include the full content of the files or copy the summary to the clipboard.

    Command Line Arguments:
        project_path (str): The file path to the root of the Python project. Defaults to the current directory.
        -o, --output-filepath (str): Path to save the generated summary. If not specified, outputs to the console.
        -r, --readme (flag): Include the project's README.md content in the summary.
        -i, --inspection (flag): Include a summary of functions and classes in the project.
        -d, --docstrings (flag): Include docstrings in the summary of functions and classes. Requires inspection flag.
        -f, --full-content (flag): Include the full content of all files in the summary.
        -cb, --clipboard (flag): Copy the generated summary to the clipboard.

    The function sets flags for including various components in the summary based on the user input.
    If no specific features are requested, it defaults to including all features in the summary.

    Example Usage:
        codescope /path/to/project -o output.txt -t -r -i -d -cb

    This will generate a summary of the project at '/path/to/project', including its file tree, README.md,
    a summary of functions and classes with docstrings, and copy the summary to the clipboard. The summary
    will be saved to 'output.txt'.
    """

    parser = argparse.ArgumentParser(
        description="Generates a comprehensive summary of a Python project, "
        "including file structure, README contents, and details of functions and classes."
    )
    parser.add_argument(
        "project_path",
        nargs="?",
        default=".",
        help="The file path to the root of the Python project. " "Defaults to the current directory if not specified.",
    )

    parser.add_argument(
        "-r",
        "--readme",
        action="store_true",
        help="Include the content of the README.md file in the summary."
    )
    parser.add_argument(
        "-i",
        "--inspection",
        action="store_true",
        help="Include a summary of functions and classes found in the project.",
    )
    parser.add_argument(
        "-d",
        "--docstrings",
        action="store_true",
        help="Include docstrings in the summary of functions and classes. "
        "This option is effective only if the inspection flag is also activated.",
    )
    parser.add_argument(
        "-p",
        "--prompt",
        action="store_true",
        help="Include prompt asking to summarize. "
    )
    parser.add_argument(
        "-f",
        "--full-content",
        action="store_true",
        help="Include the full content of all files in the project in the summary.",
    )

    parser.add_argument(
        "-o",
        "--output-filepath",
        type=str,
        help="The path where the generated summary should be saved. "
        "If not specified, the summary is printed to the console.",
    )
    parser.add_argument(
        "-cb",
        "--clipboard",
        action="store_true",
        help="Copy the generated summary to the clipboard."
    )
    args = parser.parse_args()

    # Determine if any specific features are requested
    specific_features_requested = args.readme or args.inspection or args.docstrings or args.full_content or args.prompt

    # Set flags based on user input or default to full features if no specific features are requested
    include_context_prompt = args.prompt if specific_features_requested else True
    include_readme = args.readme if specific_features_requested else True
    include_inspection = args.inspection if specific_features_requested else True
    include_docstrings = args.docstrings if specific_features_requested and args.inspection else include_inspection
    include_full_file_content = args.full_content

    summary = compile_project_summary(
        project_path=args.project_path,
        include_tree=True,
        include_inspection=include_inspection,
        include_readme=include_readme,
        include_docstrings=include_docstrings,
        include_context_prompt=include_context_prompt,
        include_full_file_content=include_full_file_content,
    )
    export_summary(
        summary=summary,
        output_filepath=args.output_filepath,
        clipboard=args.clipboard,
    )


if __name__ == "__main__":
    main()
