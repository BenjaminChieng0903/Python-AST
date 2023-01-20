# Length of a string with if statement
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    # need to check that len is used to check if the string is greater than 7
    snake = "<SSSSSSSSP"
    # Student Code
    if (len(snake) > 7):
        print("True")
    else:
        print("False")
    # Student Code
    # assertions

except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be True