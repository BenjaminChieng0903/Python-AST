# Assign a value to a variable
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    student_age = 12
    # assertions
    assert student_age == 12
    
try:
    #Add things to make test work
    # Student Code
    test()
    # Student Code
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 