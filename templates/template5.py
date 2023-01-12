# Dichotomous Keys
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    # Needs to be run to test that all paths are correct
    # Need to check that the print statements are correct
    fur = False
    feathers = False
    # Student Code
    if (fur):
        print("Bat")
    elif(feathers):
        print("Bird")
    else:
        print("Insect")
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# unsure how to do this one
