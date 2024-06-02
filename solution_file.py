from pathlib import Path


def write_sols_to_file(file_name: str | Path) -> None:
    directory = None
    full_file_name = None
    with open(file_name, 'w') as file_handle:
        file_handle.write(f"Select textbook problems and their corresponding "
                          f"solutions should be written here")


def create_and_write_sols(file_name: str | Path): # Rewrite this: could be used as lambda expression and be used directly
    with open(file_name, 'x') as file_handle:
        file_handle


if __name__ == '__main__':
    pass
