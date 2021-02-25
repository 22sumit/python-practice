def ExceptionHandling(a,b):
    try:
        d=a//b
        print(d)
    except ArithmeticError:
        print("Exception: Can't divide by 0")
    finally:
        print("finally program finished")

ExceptionHandling(10,0)