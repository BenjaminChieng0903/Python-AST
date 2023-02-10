# ASCII Art with new line
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    print('What is it that can\'t be done with patience?')

try:
    #Add things to make test work
    # need to make sure that the characters are escaped and not printed by using "" instead of ''
    # Student Code
    test()
    # Student Code
    # assertions

except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be  What is it that can't be done with patience?