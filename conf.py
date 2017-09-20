import os


def getenv(name, default=None):
    value = os.getenv(name, default)
    if value is None:
        raise KeyError('Environment variable {name} should be provided'.format(name=name))
    return value


CHECKER_KEY_FILENAME = getenv('CHECKER_KEY_FILENAME')

