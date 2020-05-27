# Write a Python program to print to stderr.

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("foo", "bar", "baz", sep="---")