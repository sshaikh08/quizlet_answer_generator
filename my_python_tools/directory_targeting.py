from os import path


def check_for_directory(operating_sys: str,
                        target_parent_dic: str,
                        target_path_ext: str) -> bool:
    documents_path = path.join('~', 'Documents')

    target_path =

    does_path_exist = path.exists(target_path)

    return does_path_exist
