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

def number1(num):
    global functionCallCount
    functionCallCount += 1
    assert_true(num >= 0, "Your recursive function did not implement stop condition at num == 0")
    return 0 if num == 0 else 1 + number1(num - 1)
try:
    assert_true(number1(0) == 0, "The function number with 0 as argument should return 0.")
    assert_true(functionCallCount == 1, "number(0) should be setup as the base case for recursion.")
    assert_true(number1(2) == 2, "The function number with 2 as argument should return 2.")
    assert_true(functionCallCount == 4, "number(2) should call itself two more times.")
    print("111")
except NameError as nameerror:
    eprint(nameerror)
except Internal_Explanation as e:
    eprint(e)