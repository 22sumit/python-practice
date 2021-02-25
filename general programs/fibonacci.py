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
        n1=n2
        n2=m
        count+=1