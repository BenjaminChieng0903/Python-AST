# Assign multiple a values to variables in a single line 
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    wheat, rice, apple, oranges, grapes = 20, 100, 34, 27, 12
    # assertions
    assert wheat == 20
    assert rice == 100
    assert apple == 34
    assert oranges == 27
    assert grapes == 12
    
try:
    #Add things to make test work
    # Need to make sure that all variables are assigned in a single line 
    # Student Code
    test()
    # Student Code
    
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 