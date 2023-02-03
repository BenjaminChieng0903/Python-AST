# Single print assign variable
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    try:
        #Add things to make test work
        # Student Code
        word = "RAIN"
        print(word)
        # Student Code
        # assertions
        assert word == "RAIN"
    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code

    # stdout should be RAIN