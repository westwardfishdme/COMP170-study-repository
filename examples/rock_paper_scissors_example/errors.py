import sys


# prints out to STDERR
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
