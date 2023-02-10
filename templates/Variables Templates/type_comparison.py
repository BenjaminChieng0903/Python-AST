# Compare the types variables
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test(fish, boat):
    print(type(fish) == type(boat)) 
    
try:
    #Add things to make test work
    fish = 45
    boat = 20.6
    # Student Code
    test(fish, boat)
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be False