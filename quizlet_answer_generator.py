import sys

WELCOME_MESSAGE = "Welcome to the Quizlet Solutions Generator"


def confirm_file_name(file_name_input: str) -> None:
    accept_file_name_values = ('Y', 'N')
    print(f"You have entered \"{file_name_input}\". Do you wish to keep this name? (Y/N) ",
          end='')  # Code Review: Is there a better practice?
    while True:
        try:
            accept_file_name = input()
            if not accept_file_name.strip() and accept_file_name.upper() not in accept_file_name_values:
                raise ValueError
        except ValueError as e:
            print("Please enter Y or N: ", end=' ')


def get_file_name() -> str:  # Code Review: I'm guessing there is a modernized/better way to do this?
    print("Please enter a file name:", end=' ')
    while True:
        try:
            file_name_entered = input().strip()
            if not file_name_entered:
                raise ValueError
        except ValueError as e:
            print("Please enter a valid file name:", end=' ')
            continue

        # noinspection PyUnboundLocalVariable
        confirm_file_name(file_name_entered)  # Code Review: Is this okay? Pycharm was throwing a warning but the
        # preceding comment tells pycharm to ignore it
        break

    return file_name_entered


if __name__ == '__main__':
    print(f"{WELCOME_MESSAGE}")

    file_name = get_file_name()

    print(f"{file_name}")

    sys.exit(0)
