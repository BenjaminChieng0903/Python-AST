# Assign a value to a variable
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    ants = 0
    flies = 10
    grasshoppers = 0
    # Student Code
    ants = ants + 30
    flies = flies - 3
    grasshoppers = grasshoppers + 3
    # Student Code
    # assertions
    assert ants == 30
    assert flies == 7
    assert grasshoppers == 3
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 