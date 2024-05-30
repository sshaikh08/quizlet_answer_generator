from sys import exit

from my_python_tools.file_targeting import get_file_name
from my_python_tools.directory_targeting import check_for_directory

WELCOME_MESSAGE = "Welcome to the Quizlet Solutions Generator"

if __name__ == '__main__':
    print(WELCOME_MESSAGE)

    check_for_directory('Documents')

    solutions_file_name = get_file_name()

    exit(0)  # Code Review: Is this correct usage? Trying to formally end the program
