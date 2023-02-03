# Concatenation
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
   
def test(): 
    try:
        #Add things to make test work
        # need to check that the two strings are concatenated and that the string isn't just written out in its entirety
        # Student Code
        print("Rea" + "son")
        # Student Code
        # assertions

    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code

    # stdout should be Reason