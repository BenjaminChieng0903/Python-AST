import sys

class Internal_Explanation(Exception):

    def __init__(self, message):
        super().__init__(f"Explanation: {message}")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def assert_true(condition, message):
    if not condition:
        raise Internal_Explanation(message)

def area1(length):
    return length * length
try:
    assert_true(area1(2) == 4, "Area of a square of length 2 must be 4. Check your code")
    assert_true(area1(3) == 9, "Area of a square of length 3 must be 9. Check your code")
    assert_true(area1(10) == 100, "Your code does not work with general bigger number. Try following the formula")
    print("Passed")
except NameError as nameerror:
    eprint(nameerror)
except Internal_Explanation as e:
    eprint(e)