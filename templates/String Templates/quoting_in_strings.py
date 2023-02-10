# Quoting in strings
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    yearbook = "Elle, 'El'"
    print(yearbook)
    # assertions
    assert yearbook == "Elle, 'El'"
    
try:
    #Add things to make test work
    # Student Code
    test()
    # Student Code
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be Elle, 'El'