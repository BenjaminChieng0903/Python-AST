# Print an expression
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test(a, b):
    print(a % b)
        
try:
    #Add things to make test work
    # Need to check that the variables are used
    a = 12
    b = 8
    # Student Code
    test(a, b)
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 4