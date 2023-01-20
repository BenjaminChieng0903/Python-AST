# Single line boolean expression
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    # Need to check that the statement is exactly correct as these questions recreate the worded expression
    Algeria = 2.3
    Argentina = 2.7
    expr = (
        # Student Code
        Algeria != Argentina
        # Student Code
    )
    # assertions
    assert expr == True
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be True