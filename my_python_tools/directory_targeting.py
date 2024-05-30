from os import path, mkdir
from sys import exit


def check_for_directory(directory_path: str) -> None:
    try:
        if not path.exists(directory_path):
            raise FileNotFoundError

    except FileNotFoundError as fe:
        print(f"The {directory_path} does not exist."
              f"\n"
              f"Check if the enter path exists and try again")
        exit(1)


# Code Review: Check for a better way
#              Is this redundant? or use try/except with os.makedirs?
#              Using os.mkdir makes more sense to me
def check_and_create_dir(dir_path: str) -> None:
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
        test_folder_instance = 0
        test_folder_main_title = 'test_folder'

        while True:
            try:

