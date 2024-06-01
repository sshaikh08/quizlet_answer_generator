from os import path
from pathlib import Path
from sys import exit

from my_python_tools.file_targeting import get_file_name
from my_python_tools.directory_targeting import check_for_directory, check_and_create_dir

WELCOME_MESSAGE = "Welcome to the Quizlet Solutions Generator"
home_dir_path = path.expanduser('~')
target_main_dir = Path(path.join(home_dir_path, 'Documents'))  # Documents Directory Path

quizlet_svd_dir_pth = Path.joinpath(target_main_dir, 'quizlet_saved_solutions')

if __name__ == '__main__':
    print(WELCOME_MESSAGE)

    check_for_directory(target_main_dir)  # Rewrite this: make the argument type entered stronger. Possibly write this in a
#                                           way that one variable can be passed into multiple items.
#                                           And for somthing like filenames and directory
#                                           paths are stored in variables in a hierarchy according to path name.
#                                           That way variables can be passed in to multiple functions to work in
#                                           coordination with multiple functions called in that particular module.
#                                           Use the library "Shelve" in rewrite.

    check_for_directory(quizlet_svd_dir_pth)

    solutions_file_name = get_file_name()

    target_file_path = path.join(target_main_dir, solutions_file_name)

    exit(0)  # Code Review: Is this correct usage? Trying to formally end the program
