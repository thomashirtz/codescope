from pathlib import Path
from typing import Optional

from clipboard import copy


def export_summary(summary: str, output_filepath: Optional[str], clipboard: bool) -> None:
    """
    Outputs the given project summary to a file, clipboard, or console.

    This function supports multiple modes of output for the project summary. It can write the summary
    to a specified file path, copy it to the clipboard, or print it to the console, based on the provided arguments.

    Args:
        summary (str): The project summary to be output.
        output_filepath (Optional[str]): The file path where the summary is to be written. If None, prints to the console.
        clipboard (bool): If True, the summary is also copied to the clipboard.

    Raises:
        FileNotFoundError: Raised if the specified file path does not exist.
        PermissionError: Raised if there is a permission issue writing to the file.
        IOError: Raised for other I/O related errors.
    """
    if clipboard:
        copy(summary)
        print("Summary copied to clipboard.")

    if output_filepath:
        try:
            with Path(output_filepath).open("w") as file:
                file.write(summary)
            print(f"Summary written to {output_filepath}")
        except FileNotFoundError:
            print(f"Error: The file path {output_filepath} does not exist.")
        except PermissionError:
            print(f"Error: Permission denied when writing to {output_filepath}.")
        except IOError as e:
            print(f"Error writing summary to file: {e}")
    else:
        print(summary)
