# Single line boolean expression
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def test(Algeria, Argentina):    
    Algeria != Argentina
    
try:
    #Add things to make test work
    # Need to check that the statement is exactly correct as these questions recreate the worded expression
    Algeria = 2.3
    Argentina = 2.7
    
    # Student Code
    test(Algeria, Argentina)
    
    Algeria = 2.7
    Argentina = 2.3
    test(Algeria, Argentina)
    # Student Code
    
    # assertions
    
except Exception as e:
        eprint(e)

        
# Test stdout, stderr, and exit code

# stdout should be True