from sys import exit

from user_input import get_file_name


if __name__ == '__main__':
    solutions_file_name = get_file_name()

    exit(0) # Code Review: Is this correct usage? Trying to formally end the program
