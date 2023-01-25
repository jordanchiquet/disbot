from randomhelpers import genErrorHandle


def genErrorHandleTest():
    print("Trying to get non global")
    try:
        print(cantGet)
    except Exception as e:
        genErrorHandle(e)
    finally:
        print("done")


genErrorHandleTest()