from sys import exit

from my_python_tools.user_input import get_file_name

WELCOME_MESSAGE = "Welcome to the Quizlet Solutions Generator"

if __name__ == '__main__':
    solutions_file_name = get_file_name()

    exit(0)  # Code Review: Is this correct usage? Trying to formally end the program
