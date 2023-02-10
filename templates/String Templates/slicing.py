# Convert to string
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test(water):
    ans = water[3:7]
    # assertions
    assert ans == "dust"
    
try:
    #Add things to make test work
    
    water = "tapdustwater"
    # Student Code
    test(water)
    # Student Code

except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 