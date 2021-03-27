lower = 50
upper = 100
l=[]
count=0
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   for i in range(2, num//2):
       if (num % i) == 0:
           count=1
           break
       else:
        l.append(num)
        count=0
print (l)