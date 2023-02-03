# Multiple if statements
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    try:
        #Add things to make test work
        # Need to check that both if statements are correct as this is a multiple if statement used before the else statement is taught
        payload1 = 2.1
        payload2 = 1.2
        budget = 20
        # Student code
        if (payload1 < payload2):
            budget -= payload1
        if (payload2 < payload1):
            budget -= payload2
        # assertions
        assert budget == 18.8
    except Exception as e:
            eprint(e)

    # Test stdout, stderr, and exit code
