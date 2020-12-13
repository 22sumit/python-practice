# A number whose cube of digits equals the number itself ex 0, 1, 153, 370, 371 and 407
n=370
s=0
k=n
while(k>0):
    a=k%10
    k=k//10
    s=s+a*a*a

print("Armstrong Number") if n==s else print("Non amstrong Number")
