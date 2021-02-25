# Method 1
s="assassination"
l1=[{i:s.count(i)} for i in set(s)] #list comprehension
print(l1)
s1={i:s.count(i) for i in s} #set comprehension
print(s1)

#Method 2
d={}
for char in s:
    if char in d.keys():
        d[char]+=1
    else:
        d[char]=1
print(d)