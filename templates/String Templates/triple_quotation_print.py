# String repetition print 
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
def test():
    print('''The sun shines bright in the sky,
the clouds pass by,
the birds sing sweetly in harmony,
on a blissful summer's day.''')
    
try:
    #Add things to make test work
    # need to check that the string is printed across multiple lines
    # Student Code
    test()
    # Student Code
    # assertions
except Exception as e:
        eprint(e)

# Test stdout, stderr, and exit code

# stdout should be 
# The sun shines bright in the sky,
# the clouds pass by,
# the birds sing sweetly in harmony,
# on a blissful summer's day. 
