import functools
import sys
import traceback


def genFuncErrorWrapper(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            genErrorHandle(e)
    return(wrapper)

def genErrorHandle(exception: Exception) -> str:
    exceptionType = type(exception).__name__
    tb = sys.exc_info()[-1]
    stack = traceback.extract_tb(tb, 1)
    functionName = stack[0][2]
    outStr = (f"ERROR:{functionName}:{exceptionType}:{exception}")
    print(outStr)
    return(outStr)

@genFuncErrorWrapper
def testFunc(test: str):
    print(f"testFunc called with {test}")
    if test:
        print("test is true")
    else:
        raise Exception("test is false")

testFunc()