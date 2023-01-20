# Print a string using a for loop
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    string = "puppy"
    # Student Code
    for element in string:
        print(element, end=' ')
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be p u p p y