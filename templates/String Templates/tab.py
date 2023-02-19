# patterns with tab
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    pattern = "||||||||| \n\t||||||||| \n\t\t||||||||| \n\t\t||||||||| \n\t||||||||| \n|||||||||"
    print(pattern)
    # assertions
    assert pattern == "||||||||| \n\t||||||||| \n\t\t||||||||| \n\t\t||||||||| \n\t||||||||| \n|||||||||"
    
try:
    #Add things to make test work
    # Student Code
    test()
    # Student Code
    
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