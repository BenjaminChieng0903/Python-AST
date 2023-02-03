# Print a variable using the str function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    try:
        #Add things to make test work
        # Need to check that the variable is printed an not just a written string
        # Student Code
        sentence = "The car costs "
        number = 20000
        print(str(sentence) + str(number))
        # Student Code
        # assertions
    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code

    # stdout should be The car costs 20000