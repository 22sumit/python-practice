n=int(input("Enter a number: "))
count=0
for i in range(2,n//2):
    if n%i==0:
        count=1
        break
print("Prime number") if count==0 else print("non prime number")