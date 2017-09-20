CHECKER_KEY_FILENAME = 'checker_key.pub'


def parse_key(key_file_content):
    return key_file_content


def read_key(key_file_name):
    with open(key_file_name) as f:
        key_file_content = f.read()
    return parse_key(key_file_content)


CHECKER_KEY = read_key(CHECKER_KEY_FILENAME)
