import re

ip="10.119.255.0"
aa=re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",ip)
print(aa)

#Working Method
l=ip.split('.')
print(l)
count=0
for i in l:
    if (int(i)<256 and int(i)>=0):
        count=0
    else:
        count=1
        break

print("valid") if count==0 else print("invalid")
