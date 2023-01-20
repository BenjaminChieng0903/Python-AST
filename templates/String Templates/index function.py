# Return the index of the first occurrence of a substring in a string
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    race = "]---O-"
    # Student Code
    position = race.index("O")
    print(position)
    # Student Code
    # assertions
    assert position == 5, "position should be 5"
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 4