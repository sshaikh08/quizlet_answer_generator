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


def confirm_file_name(file_name_input: str) -> bool:
    accept_file_name_values = {'Y': True, 'N': False}
    print(f"You have entered \"{file_name_input}\". Do you wish to keep this name? (Y/N)",
          end=' ')  # Code Review: Is there a better practice?
    while True:
        try:
            accept_file_name = input()
            if not accept_file_name.strip() or accept_file_name.upper() not in accept_file_name_values.keys():
                raise ValueError
        except ValueError as e:
            print("Please enter Y or N: ", end=' ')
        else:
            return accept_file_name_values[accept_file_name.upper()]


# Code Review: I'm guessing there is a modernized/better way to do this? I.e. getting a name from the user, and verifying
#              that the name is valid or not already taken in some capacity, in this case, a file with name entered that
#              already exists?
def get_file_path(dir_to_save_file, file_type_ext) -> str:
    enter_filename_msg = "Please enter a file name:"
    reenter_filename_msg = "Please enter a valid file name:"

    print(enter_filename_msg, end=' ')
    while True:
        try:
            file_name_entered = input().strip()
            #                                                                Code Review: Is there a better way to do
            #                                                                             this. I was going to create a
            #                                                                             dictionary with file types and
            #                                                                             their corresponding file
            #                                                                             extensions.

            full_filename = file_name_entered + '.' + file_type_ext
            file_named_path = path.join(dir_to_save_file, full_filename)
            if not file_name_entered:
                raise ValueError
            if check_path_exists(file_named_path): # Code Review: Why is pycham throwing me a warning. The warning
            #                                       is conveying that file_name_path is not of type str or Path but rather
            #                                       'LiteralString | str | bytes. Not sure what this means
                raise FileExistsError

        # Code Review: Is there a way to consolidate this?
        except ValueError as e:
            print(reenter_filename_msg, end=' ')
            continue
        except FileExistsError as fe:
            # noinspection PyUnboundLocalVariable
            print(f"A file with the name \"{file_name_entered}\" already exists"
                  f"\n"
                  f"{reenter_filename_msg}", end=' ')
            continue

        # noinspection PyUnboundLocalVariable
        if confirm_file_name(file_name_entered):  # Code Review: Is this okay? Pycharm was throwing a warning but the
        #                                           preceding comment tells pycharm to ignore it
            break
        else:
            print(enter_filename_msg, end=' ') # Code Review: Is there a better to invoke this? I wanted to start the
            # the loop over with the original "Enter a filename" message
            continue

    return file_named_path


if __name__ == '__main__':
    # Quick copy Paste Values: True, False
    home_dir = path.expanduser('~')

    check_path_exists_test_1 = False
    check_path_exists_test_2 = False
    check_path_exists_test_3 = False

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
        file_name = get_file_path()
        print(f"{file_name}")
