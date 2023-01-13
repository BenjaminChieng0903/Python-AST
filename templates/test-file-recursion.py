import sys

class Internal_Explanation(Exception):
    def __init__(self, message):
        super().__init__(f"Explanation: {message}")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def assert_true(condition, message):
    if not condition:
        raise Internal_Explanation(message)

functionCallCount = 0

def number(num):
    # Hidden variable to determine recursion depth
    global functionCallCount
    functionCallCount += 1
    # Assertion to determine stop condition for recursion
    assert_true(num >= 0, "Your recursive function did not implement stop condition at num == 0")
    # return 0 if num == 0 else 1 + number(num - 1)
    # return 0 if num == 0 else 1 if num == 1 else 2 + number(num - 2)
    # Student Code
    return 0 if num == 0 else 1 + number(num - 1)
    #return 0 if num == 0 else 1 if num == 1 else 2 + number(num - 2)
    # Student Code

try:
    # Public test
    assert_true(number(0) == 0, "The function number with 0 as argument should return 0.")
    assert_true(functionCallCount == 1, "number(0) should be setup as the base case for recursion.")
    assert_true(number(2) == 2, "The function number with 2 as argument should return 2.")
    assert_true(functionCallCount == 4, "number(2) should call itself two more times.")

    print("Passed")
except NameError as nameerror:
    eprint(nameerror)
except Internal_Explanation as e:
    eprint(e)