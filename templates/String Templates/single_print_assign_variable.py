# Single print assign variable
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    word = "RAIN"
    print(word)
    # assertions
    assert word == "RAIN"
    
try:
    #Add things to make test work
    # Student Code
    test()
    # Student Code
    
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be RAIN