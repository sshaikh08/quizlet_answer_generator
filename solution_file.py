def write_sols_to_file(file_name: str) -> None:
    directory = None
    full_file_name = None
    with open(file_name, 'w') as file_handle:
        file_handle.write(f"Select textbook problems and their corresponding "
                          f"solutions should be written here")


if __name__ == '__main__':
    pass