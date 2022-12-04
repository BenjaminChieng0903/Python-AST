import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def moveForward():
    new_move = 1000
    moveF2 = 2
    moveF = new_move + moveF2
    print('F', new_move, moveF)

def moveBackward():
    moveBB = 2
    print('B', moveBB)

def turnLeft():
    turnL2 = 3
    print('L', turnL2)

def turnRight():
    turnR = 4
    print('R', turnR)

def collectGoal():
    collect = 5
    print('G', collect)
try:
    moveForward()
    turnRight()
    moveForward()
    moveForward()
    moveForward()
    collectGoal()
    moveForward()
    collectGoal()
except Exception as e:
    eprint(e)