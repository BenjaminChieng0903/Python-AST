# Length of a string
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    try:
        #Add things to make test work
        # need to check that len is used and that 10 isn't just written out
        snake = "<SSSSSSSSP"
        # Student Code
        print(len(snake))
        # Student Code
        # assertions

    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code

    # stdout should be 10