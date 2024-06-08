from os import path
from pathlib import Path
from sys import exit

from my_python_tools.file_targeting import get_file_path
from my_python_tools.directory_targeting import check_for_directory, check_and_create_dir

WELCOME_MESSAGE = "Welcome to the Quizlet Solutions Generator"
home_dir_path = path.expanduser('~')
target_main_dir = Path(path.join(home_dir_path, 'Documents'))  # Documents Directory Path

quizlet_svd_sols_pth = Path.joinpath(target_main_dir, 'quizlet_saved_solutions')

if __name__ == '__main__':
    print(WELCOME_MESSAGE)

    check_for_directory(directory_path=target_main_dir)  # Rewrite this: make the argument type entered stronger. Possibly write this in a
    #                                       way that one variable can be passed into multiple items.
    #                                       And for somthing like filenames and directory
    #                                       paths are stored in variables in a hierarchy according to path name.
    #                                       That way variables can be passed in to multiple functions to work in
    #                                       coordination with multiple functions called in that particular module.
    #                                       Use the library "Shelve" in rewrite.

    # Code Review: I'm passing quizlet_svd_sols_path in multiple functions.
    # Are there different ways to handle this situation,
    # AKA: Mentioning the variable once that somehow passes to both functions at once instead of having to mention the
    # variable again in order to pass it into the second function?

    check_and_create_dir(dir_path=quizlet_svd_sols_pth)

    solutions_file_path = get_file_path(dir_to_save_file=quizlet_svd_sols_pth, file_type_ext='txt')



    exit(0)  # Code Review: Is this correct usage? Trying to formally end/exit the program
