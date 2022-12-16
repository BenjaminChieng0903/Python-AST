import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def moveForward():
    new = 1000
    moveF2 = 2
    moveF = new + moveF2
    print('M', new, moveF)
    print('666')

def moveBackward():
    moveBB = 2
    moveB = 10 - moveBB
    moveC = 9 - moveBB
    moveD = 10 + moveBB
    if moveD <= moveB:
        print('bb')
    elif moveD == moveB:
        print('B', moveBB)

def turnLeft():
    turnLL = 3
    print('L', turnLL)

def turnRight():
    turnR = 4
    print('R', turnR)

def collectGoal():
    col = 5
    print('G', col)
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