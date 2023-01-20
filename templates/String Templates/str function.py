# Convert to string
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    
    total = 5
    # Student Code
    receipt = "$" + str(total)
    print(receipt)
    # Student Code
    # assertions
    assert receipt == "$5"
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be $5