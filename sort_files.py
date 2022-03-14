import glob
import os
import time
from typing import List

import click


# @click.command()
# @click.option("--dir_name", default=1, help="Number of greetings.")
def sort_files_by_date(
    dir_name: str,
    reverse: bool = False,
    recursive: bool = False,
    verbose: bool = False,
) -> List[str]:
    """List files in a folder, based on date last modified

    :param dir_name: Directory to search for files
    :param reverse: Display last modified at bottom if reverse=Fasle (defualt), else top
    :param recursive: If search for last modified files should be searched recursively
    :param verbosity: If the modified files and date should be displayed
    :return: List of the files in the order specified

    $ python sort_files.py
    03/14/2022 :: 13:38:27  --> models/epoch=1-step=1072.ckpt
    03/14/2022 :: 13:39:33  --> models/epoch=3-step=1071.ckpt
    03/14/2022 :: 13:41:30  --> models/epoch=3-step=1071_1.ckpt
    """

    # Get list of all files only in the given directory
    dir_name = dir_name if dir_name.endswith("/") else f"{dir_name}/"
    list_of_files = filter(
        os.path.isfile, glob.glob(dir_name + "*", recursive=recursive)
    )
    files = sorted(list_of_files, key=os.path.getmtime, reverse=reverse)

    if verbose:
        for file_path in files:
            timestamp_str = time.strftime(
                "%m/%d/%Y :: %H:%M:%S", time.gmtime(os.path.getmtime(file_path))
            )
            print(timestamp_str, " -->", file_path)

    return files


if __name__ == "__main__":
    files = sort_files_by_date("models", verbose=True)
    print(files[-1])
