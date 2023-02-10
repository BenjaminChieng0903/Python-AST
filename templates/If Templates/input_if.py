# User input with if statement
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    answer = input("When did World War 2 end: ")
    if (answer == "1945"):
        print("Correct")
    else:
        print("Incorrect :(")
try:
    #Add things to make test work
    # The input statement may need to be changed in the question as it will be difficult to test
    # Student code
    test()
    # assertions
    
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code
