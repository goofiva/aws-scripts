import aws_scripts


def test_base64():
    encoded = aws_scripts.helpers.encrypt.encode_base64(in_str='testing')
    print(encoded)


def test_base64_file_path():
    encoded = aws_scripts.helpers.encrypt.encode_base64(file_path='./tests/files/test__helpers__encrypt/test_file.txt')
    print(encoded)
