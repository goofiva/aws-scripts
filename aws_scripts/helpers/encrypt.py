import os
import base64

def encode_base64(in_str: str=None, file_path: str=None) -> bytes:
    """

    :param in_str:
    :param file_path:
    :return:
    """
    if in_str:
        encoded = base64.b64encode(bytes(in_str, encoding='utf-8'))
        return encoded

    elif file_path:
        file_path = os.path.abspath(file_path)
        f = open(file_path, "r")
        file_content = f.read()
        f.close()
        encoded = base64.b64encode(bytes(file_content, encoding='utf-8'))
        return encoded
