# Split a string into maximum number of unique substrings

s = "ababccc"
l=[]
a=""
for i in s:
    if i not in l:
        l.append(i)
    else:
        a=a+i
        if a not in l:
            l.append(a)
            a=""

print(l)
print("max no. of unique substrings: ",len(l))