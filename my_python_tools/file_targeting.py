from os import path
from pathlib import Path


# Code Review: Check for a better way (Q.To do what? I'm assuming you mean checking unique and context
#              valid info for USER PROVIDED name

def check_path_exists(path_name: str | Path) -> bool:
    home_dir_path = path.expanduser('~')
    dir_path = path.join(home_dir_path, path_name)

    return path.exists(dir_path)


def check_and_create_file(file_name) -> None:
    pass


def confirm_file_name(file_name_input: str) -> None:
    accept_file_name_values = ('Y', 'N')
    print(f"You have entered \"{file_name_input}\". Do you wish to keep this name? (Y/N)",
          end=' ')  # Code Review: Is there a better practice?
    while True:
        try:
            accept_file_name = input()
            if not accept_file_name.strip() or accept_file_name.upper() not in accept_file_name_values:
                raise ValueError
        except ValueError as e:
            print("Please enter Y or N: ", end=' ')
        else:
            break


def get_file_name(dir_to_save_file) -> str:  # Code Review: I'm guessing there is a modernized/better way to do this?
    reenter_filename_msg = "Please enter a valid file name:"

    print("Please enter a file name:", end=' ')
    while True:
        try:
            file_name_entered = input().strip()
            file_name_path = path.join(dir_to_save_file, file_name_entered)
            if not file_name_entered:
                raise ValueError
            if check_path_exists(file_name_path):
                raise FileExistsError

        except ValueError as e:
            print(reenter_filename_msg, end=' ')
            continue
        except FileExistsError as fe:
            print(f"A file with the name \"{file_name_entered}\" already exists"
                  f"\n"
                  f"{reenter_filename_msg}", end=' ')
            continue

        # noinspection PyUnboundLocalVariable
        confirm_file_name(file_name_entered)  # Code Review: Is this okay? Pycharm was throwing a warning but the
        # preceding comment tells pycharm to ignore it
        break

    # noinspection PyUnboundLocalVariable
    return file_name_entered


if __name__ == '__main__':
    home_dir = path.expanduser('~')

    check_path_exists_test_1 = False
    check_path_exists_test_2 = True
    check_path_exists_test_3 = True

    if check_path_exists_test_1:  # Rewrite this: I think these lambda expressions here for repeating
        #                           logic used in [if statements] or test definitions
        documents_path = path.expanduser('~/Documents')
        documents_dir_exists = check_path_exists(documents_path)
        print(f"documents_dir_exists is {documents_dir_exists}")

    if check_path_exists_test_2:
        test_path = path.expanduser('~/Documents/quizlet_saved_solutions/test_file_name_1')
        test_path_exists = check_path_exists(test_path)

    if check_path_exists_test_3:
        test_path = path.expanduser('~/Documents/quizlet_saved_solutions/test_file_name_2')
        test_path_exists = check_path_exists(test_path)

    get_file_name_test_1 = False

    if get_file_name_test_1:
        file_name = get_file_name()
        print(f"{file_name}")
