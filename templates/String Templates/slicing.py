# Convert to string
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    
    water = "tapdustwater"
    # Student Code
    ans = water[3:7]
    # Student Code
    # assertions
    assert ans == "dust"
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 