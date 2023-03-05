import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    if a == b:
        print("666")

def moveForward1():
    move11 = 0
    move3 = move11
    move11 = move11 + move3
    print("FFFFF")



def moveBackward():
    print("B")

def turnLeft():
    print("L")

def turnRight():
    print("R")

def collectGoal():
    print("G")
try:
    moveForward1()
    turnRight()
    moveForward1()
    moveForward1()
    moveForward1()
    collectGoal()
    moveForward1()
    collectGoal()
except Exception as e:
    eprint(e)