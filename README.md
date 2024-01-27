# 💻 `codescope`

## Overview
`codescope` is a Python tool that creates a comprehensive summary of a Python project. It's designed for developers, teams, and even Language Learning Models (LLMs) who want to quickly understand the structure and contents of a new or existing Python project. The tool can be particularly useful for LLMs to quickly have context for a conversation about a codebase. It analyzes the project structure, including its files and directories, and extracts key information such as functions, classes, and their respective docstrings.

## Features
- **Project Overview**: Includes content from the project's README.md.
- **File Tree Structure**: Generates a tree view of the project's file structure.
- **Functions and Classes Summary**: Lists all functions and classes in the project, with the option to include docstrings.
- **Command-Line Interface**: An easy-to-use CLI for generating project summaries.

## Installation
To install codescope, you will need Python installed on your system. Then, codescope can be easily installed using pip by running the following command:

```
pip install git+https://github.com/thomashirtz/codescope#egg=codescope
```

This command will install the latest version of codescope directly from the GitHub repository. Once installed, you can utilize the application via the command line using `codescope` or `cs`.

## Usage
The tool is used via the command line with various flags to customize the output:

Positional Arguments:
- `project_path`: Path to the Python project (optional, defaults to the current directory if not specified).

Optional Flags:
- `-o`, `--output-filepath`: Specify the output file path.
- `-r`, `--readme`: Include project markdown (README.md) in the summary.
- `-i`, `--inspection`: Include inspection of functions and classes.
- `-d`, `--docstrings`: Include docstrings of functions and classes (only valid if inspection is activated).
- `-f`, `--full-content`: Include the full content of all files in the project in the summary.
- `-cb`, `--clipboard`: Copy the summary to the clipboard.


## Example

This section provides an example to illustrate how to use this project effectively.

<details>
<summary><b>Utilization of codescope on this project:</b></summary>


```bash
codescope . -i -d -cb
```


```
Project Structure:
/
    .flake8
    .gitignore
    codescope/
        analyzers/
            code_structure.py
            file_content.py
            hierarchy.py
            readme.py
            __init__.py
        config.py
        core.py
        utilities.py
        __init__.py
        __main__.py
    LICENSE
    pyproject.toml
    README.md
    requirements.txt
    setup.cfg
    setup.py

---

Key Functions and Classes:

In setup.py:


In codescope\config.py:

Function: `is_hidden_directory`
  Docstring: ```Check if a directory is hidden.
    
    Args:
        path (Path): The Path object of the directory.
    
    Returns:
        bool: True if it's a hidden directory, False otherwise.```

Function: `is_excluded_directory`
  Docstring: ```Check if a directory is in the excluded directories list or custom exclusions.
    
    Args:
        path (Path): The Path object of the directory.
        custom_exclusions (Optional[List[str]]): Custom directories to exclude.
    
    Returns:
        bool: True if it's an excluded directory, False otherwise.```

Function: `should_exclude_directory`
  Docstring: ```Determines whether a directory should be excluded from processing.
    
    Args:
        path (str): The path of the directory to be checked.
        custom_exclusions (Optional[List[str]]): Custom directories to exclude.
    
    Returns:
        bool: True if the directory should be excluded, False otherwise.```


In codescope\core.py:

Function: `compile_project_summary`
  Docstring: ```Compiles a detailed summary of a Python project from various components.
    
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
        str: A string containing the compiled project summary.```


In codescope\utilities.py:

Function: `export_summary`
  Docstring: ```Outputs the given project summary to a file, clipboard, or console.
    
    This function supports multiple modes of output for the project summary. It can write the summary
    to a specified file path, copy it to the clipboard, or print it to the console, based on the provided arguments.
    
    Args:
        summary (str): The project summary to be output.
        output_filepath (Optional[str]): The file path where the summary is to be written. If None, prints to the console.
        clipboard (bool): If True, the summary is also copied to the clipboard.
    
    Raises:
        FileNotFoundError: Raised if the specified file path does not exist.
        PermissionError: Raised if there is a permission issue writing to the file.
        IOError: Raised for other I/O related errors.```


In codescope\__init__.py:


In codescope\__main__.py:

Function: `main`
  Docstring: ```Entry point for the command line interface to generate a comprehensive summary of a Python project.
    
    This function parses command line arguments to configure the generation of a project summary.
    It allows specification of the project path, output options, and various aspects of the project
    to include in the summary. The summary can be customized to include the project's file tree,
    README content, inspection of functions and classes, and their docstrings. There's also an option
    to include the full content of the files or copy the summary to the clipboard.
    
    Command Line Arguments:
        project_path (str): The file path to the root of the Python project. Defaults to the current directory.
        -o, --output-filepath (str): Path to save the generated summary. If not specified, outputs to the console.
        -t, --tree (flag): Include the project's file tree structure in the summary.
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
    will be saved to 'output.txt'.```


In codescope\analyzers\code_structure.py:

Function: `summarize_ast_item`
  Docstring: ```Extracts and formats a summary from an AST item, which can be a function or a class.
    
    Args:
        item (Union[ast.FunctionDef, ast.ClassDef]): The AST item representing a function or class.
        include_docstrings (bool): Whether to include docstrings in the summary.
        indent_level (int): The level of indentation for formatting the summary.
    
    Returns:
        str: The formatted summary of the given AST item.```

Function: `summarize_python_file`
  Docstring: ```Extracts and summarizes functions and classes from a Python file.
    
    Args:
        filepath (Path): The path to the Python file.
        include_docstring (bool): Whether to include docstrings in the summary.
    
    Returns:
        str: The summary of functions and classes in the given file.```

Function: `summarize_project_code`
  Docstring: ```Generates a summary of functions and classes for all Python files in the specified directory.
    
    Args:
        path (Union[str, Path]): The path to the directory to summarize.
        include_docstrings (bool): Whether to include docstrings in the summary.
    
    Returns:
        str: The comprehensive summary of all functions and classes in the directory.```


In codescope\analyzers\file_content.py:

Function: `extract_file_contents`
  Docstring: ```Generates a summary of the contents of all Python files in the specified directory.
    
    Args:
        path (Union[str, Path]): The path to the directory to summarize.
    
    Returns:
        str: A comprehensive summary of the contents of all Python files in the directory.```


In codescope\analyzers\hierarchy.py:

Function: `generate_file_hierarchy`
  Docstring: ```Generates a visual tree structure of the file system starting from the specified path.
    
    This function traverses the directory tree starting from the given path, creating
    a string representation of the directory and file structure. It allows for configurable
    indentation and the option to include or exclude files in the output.
    
    Args:
        path (str): The root directory from which to start generating the tree structure.
        indent_size (int): The size of the indentation for each level of the tree (default is 4).
        include_files (bool): Flag to include files in the tree structure (default is True).
    
    Returns:
        str: A string representation of the tree structure of the file system.```


In codescope\analyzers\readme.py:

Function: `get_readme_content`
  Docstring: ```Retrieves the content of the README.md file from the specified project path.
    
    Attempts to read and return the contents of README.md located in the project directory.
    If the file does not exist, a default message indicating its absence is returned.
    
    Args:
        project_path (str): The path to the project directory containing README.md.
    
    Returns:
        str: The content of README.md, or a message if the file is not found.
    
    Raises:
        FileNotFoundError: Raised if README.md does not exist at the specified path, but handled internally.```


In codescope\analyzers\__init__.py:

---

```

</details>

## Support and Community
For support, questions, suggestions or discussions, please open an issue in the GitHub repository.

## License

     Copyright 2024 Thomas Hirtz

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.

