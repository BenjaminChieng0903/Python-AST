import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
try:
    Russia = 10
    Canada = 7
    # Student Code
    if Russia > Canada:
        print('True')
    # Student Code
except Exception as e:
    eprint(e)