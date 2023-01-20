# ASCII Art with new line
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    # need to make sure that the characters are escaped and not printed by using "" instead of ''
    # Student Code
    print('What is it that can\'t be done with patience?')
    # Student Code
    # assertions

except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be  What is it that can't be done with patience?