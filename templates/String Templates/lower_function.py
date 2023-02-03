# Print a string using a for loop
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    try:
        #Add things to make test work
        # need to make sure that lower is used and that the string isn't just written out
        # Student Code
        print("Deere".lower())
        # Student Code
        # assertions
    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code

    # stdout should be deere