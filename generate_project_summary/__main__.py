import argparse
from generate_project_summary.codebase_analyzer import generate_codebase_summary


def main():
    """
    Main function to parse command line arguments and generate a project summary.

    This script provides command line arguments to specify the details of the summary generation.
    It supports including a tree view of the project, README content, and an inspection of
    functions and classes. The summary can include docstrings if both inspection and
    docstring flags are set. The summary can be output to a specified file, printed to the console,
    or copied to the clipboard.
    """
    parser = argparse.ArgumentParser(description="Generate a summary of a Python project.")
    parser.add_argument('project_path', nargs='?', default='.',
                        help='Path to the Python project. Defaults to the current directory if not specified.')
    parser.add_argument('-o', '--output-filepath', type=str, help='Output file path (optional)')
    parser.add_argument('-t', '--tree', action='store_true', help='Include file tree structure in summary')
    parser.add_argument('-r', '--readme', action='store_true', help='Include project markdown (README.md) in summary')
    parser.add_argument('-i', '--inspection', action='store_true', help='Include inspection of functions and classes')
    parser.add_argument('-d', '--docstrings', action='store_true', help='Include docstrings of functions and classes (only valid if inspection is activated)')
    parser.add_argument('-a', '--all', action='store_false', help='Include all features in summary')
    parser.add_argument('-cb', '--clipboard', action='store_true', help='Copy the summary to the clipboard')

    args = parser.parse_args()

    include_tree = args.tree or args.all
    include_readme = args.readme or args.all
    include_inspection = args.inspection or args.all
    include_docstrings = (args.docstrings or args.all) and include_inspection

    generate_codebase_summary(
        project_path=args.project_path,
        include_tree=include_tree,
        include_inspection=include_inspection,
        include_docstrings=include_docstrings,
        include_readme=include_readme,
        output_filepath=args.output_filepath,
        clipboard=args.clipboard,
    )


if __name__ == '__main__':
    main()
