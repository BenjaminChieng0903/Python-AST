import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def moveForward():
    print("F")

def moveBackward():
    print("B")

def turnLeft():
    print("L")

def turnRight():
    print("R")

def collectGoal():
    print("G")
 
try:
    # Student Code
    moveForward()
    turnRight()
    moveForward()
    moveForward()
    moveForward()
    collectGoal()
    moveForward()
    collectGoal()   
    # Student Code

except Exception as e:
    eprint(e)
