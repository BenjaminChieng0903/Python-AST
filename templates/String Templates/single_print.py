# Single line print statement
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    print("CAT")
    
try:
    #Add things to make test work
    # Student Code
    test()
    # Student Code
    # assertions

except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be CAT