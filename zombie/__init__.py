__version__ = "1.0.0"

import os

print(f"zombie 2D Game Engine version {__version__}")
BASE_DIRECTORY = os.getcwd()


def get_version():
    _version = __version__.split('.')
    return _version[0], _version[1], _version[2]
