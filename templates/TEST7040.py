import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def moveForward():
    newMove = 1000
    moveF2 = 2
    moveF = newMove + moveF2
    print('M', newMove, moveF)
    print('666')

def moveBackward():
    moveBB = 2
    moveB = 10 - moveBB
    moveC = 9 - moveBB
    moveD = 10 + moveBB
    if moveD >= moveB:
        print('bb')
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