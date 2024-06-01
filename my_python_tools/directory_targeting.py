from os import path, mkdir
from pathlib import Path
from sys import exit


# Code Review: Initially these functions only took strings, and the type hint indicated as much.
#              Is there anything wrong with being able to pass a type Path object as well with the way
#              these functions are written?
def check_for_directory(directory_path: str | Path) -> None:
    try:
        if not path.exists(directory_path):
            raise FileNotFoundError

    except FileNotFoundError as fe:
        print(f"{directory_path} does not exist." # Rewrite This: 
              f"\n"
              f"Check if the enter path exists and try again")
        exit(1)


# Code Review: Check for a better way
#              Is this redundant? or use try/except with os.makedirs?
#              Using os.mkdir makes more sense to me
def check_and_create_dir(dir_path: str | Path) -> None:
    if not path.exists(dir_path):
        print(f"{dir_path} does not exist."
              f"\n"
              f"Creating directory \"{dir_path}")
        mkdir(dir_path)


if __name__ == '__main__':

    test_1 = False
    if test_1:
        home_directory_path = path.expanduser('~')
        documents_directory = path.join(home_directory_path, 'Documents')

        check_for_directory(documents_directory)

    test_2 = False
    if test_2:
        test_2_path = Path.cwd().parent.absolute()
        print(f"Current Working Directory: {Path.cwd()}"
              f"\n"
              f"Parent Directory: {str(test_2_path)}")

        test_3_path = Path.joinpath(test_2_path, 'test_folder')

        print(f"test_3_path: {test_3_path}")

        check_and_create_dir(test_3_path)
