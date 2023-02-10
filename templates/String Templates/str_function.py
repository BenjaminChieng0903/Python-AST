# Convert to string
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test(total):
    receipt = "$" + str(total)
    print(receipt)
    # assertions
    assert receipt == "$5"
    
try:
    #Add things to make test work
    
    total = 5
    # Student Code
    test(total)
    # Student Code
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be $5