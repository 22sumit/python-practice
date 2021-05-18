# Method 1 using Recursion
def Fibonacci(n):
    if n<=1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

n = int(input("How many terms? "))
if n<=0:
    print("Enter a valid number !!")
for i in range(n):
    print(Fibonacci(i),end=" ")
print()

# Method 2
n1,n2=0,1
count=0
if n<0:
    print("Enter a valid number !!")
elif n == 0:
    print(n1)
else:
    while count<n:
        print(n1)
        m=n1+n2
        n1,n2=n2,m
        count+=1

#Method 3
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(5):
    print(fib(i))

#Method 4
def fiblist(n):
    fib = [0, 1]
    for i in range(2, n):
        fib += [fib[-1] + fib[-2]]
    return fib
print(fiblist(6))

#Method 5 using Generators
def fib_gen(n):
    x,y=0,1
    while (x<n):
        yield x
        x, y = y, x + y

for i in fib_gen(5):
    print("fibgen: ",i)

#To get the fibonacci numbers till any number (100 in this case) with generator
def fib_limit():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for i in fib_limit():
    if i>100:
        break
    print("fib_limit: ",i)