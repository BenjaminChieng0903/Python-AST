# Assign a value to a variable
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    try:
        #Add things to make test work
        # Student Code
        student_age = 12
        # Student Code
        # assertions
        assert student_age == 12
    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code

    # stdout should be 