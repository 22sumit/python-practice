l=[2,6,4,9,7,8,3,1,41,5]
s=[]
while l:
    n=l.pop()
    if (10-n) in l:
        s.append((n,10-n))

print(s)