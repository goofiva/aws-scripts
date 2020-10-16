import os

def get_file_content(file_path: str) -> str:
    """

    :param file_path:
    :return:
    """
    file_path = os.path.abspath(file_path)
    f = open(file_path, "r")
    file_content = f.read()
    f.close()
    return file_content
