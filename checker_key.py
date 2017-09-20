CHECKER_KEY_FILENAME = 'checker_key.pub'


def read_key(key_file_name):
    with open(key_file_name) as f:
        # A correctness check might be useful
        return f.read()


CHECKER_KEY = read_key(CHECKER_KEY_FILENAME)
