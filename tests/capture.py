"""
Capture function
----------------------------------

"""

# Standard library imports
import sys
from io import StringIO


def capture(func, *args, **kwds):
    sys.stdout = StringIO()  # capture output
    out = func(*args, **kwds)
    out = sys.stdout.getvalue()  # release output
    out = bytes(out, "utf8")
    return out
