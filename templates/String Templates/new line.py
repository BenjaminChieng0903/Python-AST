# ASCII Art with new line
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    # Student Code
    print("  \ \n ()() \n()()() \n ()() \n  ()")
    # Student Code
    # assertions

except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be  
#    \
#   ()()
#  ()()()            
#   ()()
#    ()