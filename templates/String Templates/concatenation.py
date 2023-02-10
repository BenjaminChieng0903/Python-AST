# Concatenation
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
   
def test(): 
    print("Rea" + "son")
    
try:
    #Add things to make test work
    # need to check that the two strings are concatenated and that the string isn't just written out in its entirety
    # Student Code
    test()
    # Student Code
    # assertions

except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be Reason