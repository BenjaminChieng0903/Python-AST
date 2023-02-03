# Quoting in strings
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    try:
        #Add things to make test work
        # Student Code
        yearbook = "Elle, 'El'"
        print(yearbook)
        # Student Code
        # assertions
        assert yearbook == "Elle, 'El'"
    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code

    # stdout should be Elle, 'El'