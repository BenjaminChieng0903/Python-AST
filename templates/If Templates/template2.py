# Single line if statement
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    # Need to check that the if statement is exactly correct 
    Russia = 10
    Canada = 7
    # Student code
    if (Russia > Canada):
        print("True")
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code
# stdout should be True