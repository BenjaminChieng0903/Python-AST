# String repetition print 
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    print("Uncopyrightable " * 7)
    
try:
    #Add things to make test work
    # need to check that string repetition is used and that the string isn't just written out
    # Student Code
    test()
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be Uncopyrightable Uncopyrightable Uncopyrightable Uncopyrightable Uncopyrightable Uncopyrightable Uncopyrightable 