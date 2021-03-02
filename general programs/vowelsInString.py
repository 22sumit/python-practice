s="this is a test to FIND vowels in A string"

#Method 1
l=[i for i in s if i in 'aeiouAEIOU']
print(l)

set1={i for i in s if i in 'aeiouAEIOU'}
print(set1)

#Method 2
s1=set()
for c in s:
    if c in "aeiouAEIOU" and c not in s1:
        s1.add(c)
print("s1: ",s1)