# patterns with tab
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
try:
    #Add things to make test work
    # Student Code
    pattern = "||||||||| \n\t||||||||| \n\t\t||||||||| \n\t\t||||||||| \n\t||||||||| \n|||||||||"
    print(pattern)
    # Student Code
    # assertions
    assert pattern == "||||||||| \n\t||||||||| \n\t\t||||||||| \n\t\t||||||||| \n\t||||||||| \n|||||||||"
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be
# 	|||||||||
# 		    |||||||||
#                   |||||||||
# 		            |||||||||                    
# 		    |||||||||           
# 	|||||||||