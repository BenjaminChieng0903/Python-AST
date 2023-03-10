# Print a variable
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test(item3):
    print(item3)
    
try:
    #Add things to make test work
    # Need to check that the variable is printed an not just a written string
    item3 = "Clothes"
    # Student Code
    test(item3)
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be Clothes