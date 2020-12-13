# Method 1
s="assassination"
l1=[{i:s.count(i)} for i in set(s)]
print(l1)

#Method 2
d={}
for char in s:
    if char in d.keys():
        d[char]+=1
    else:
        d[char]=1
print(d)