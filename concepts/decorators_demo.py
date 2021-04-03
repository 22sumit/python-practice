'''
Modify the behaviour of function at compile time.
Adds special features to an existing functionality.
'''

#Example 1
def f1(func):
    def wrapper():
        print("hi")
        func()
        print("bye")
    return wrapper()

@f1     #f = f1(f)
def f():
    print("Hello")

#Example 2

def smart_div(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            result=func(a,b)
        return result
    return wrapper

@smart_div  # div=smart_div(div)
def div(a,b):
    print(a//b)

div(2,4)