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