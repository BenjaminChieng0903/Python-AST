# Check the type of a variable
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test(fish):
    print(type(fish))
    
try:
    #Add things to make test work
    fish = 45
    # Student Code
    test(fish)
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be <class 'int'>