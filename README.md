
# generate-project-summary

## Overview
Generate Project Summary is a Python tool that creates a comprehensive summary of a Python project. It's designed for developers, teams, and even Language Learning Models (LLMs) who want to quickly understand the structure and contents of a new or existing Python project. The tool can be particularly useful for LLMs to quickly have context for a conversation about a codebase. It analyzes the project structure, including its files and directories, and extracts key information such as functions, classes, and their respective docstrings.

## Features
- **Project Overview**: Includes content from the project's README.md.
- **File Tree Structure**: Generates a tree view of the project's file structure.
- **Functions and Classes Summary**: Lists all functions and classes in the project, with the option to include docstrings.
- **Command-Line Interface**: An easy-to-use CLI for generating project summaries.

## Installation
1. Clone the repository:
   ```
   git clone https://your-repository-url.git
   ```
2. Navigate to the project directory:
   ```
   cd generate_project_summary
   ```
3. Install the package:
   ```
   pip install .
   ```

## Usage
The tool is used via the command line with various flags to customize the output:

Positional Arguments:
- `project_path`: Path to the Python project (optional, defaults to the current directory if not specified).

Optional Flags:
- `-o`, `--output-filepath`: Specify the output file path.
- `-t`, `--tree`: Include file tree structure in the summary.
- `-r`, `--readme`: Include project markdown (README.md) in the summary.
- `-i`, `--inspection`: Include inspection of functions and classes.
- `-d`, `--docstrings`: Include docstrings of functions and classes (only valid if inspection is activated).
- `-a`, `--all`: Include all features in the summary.
- `-cb`, `--clipboard`: Copy the summary to the clipboard.

Example command:
```
gps -p /path/to/project -o output.txt -a
```

## Troubleshooting
- If you encounter [issue], try [solution].

## Contributing
Contributions are welcome! Please follow the standard fork, branch, and pull request workflow.

## Support and Community
For support, questions, or discussions, please open an issue in the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thanks to all the contributors who have helped with this project.
