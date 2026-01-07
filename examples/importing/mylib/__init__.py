"""
This file is a seperate library
"""
from . import myotherfile


def func():
    print("call was made to mylib!")
    # test other python files in this directory:
    myotherfile.some_other_func()
    print("! func ends...")
