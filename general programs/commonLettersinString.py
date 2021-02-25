# Check Common Letters in Two Input Strings
s1="asqwwerqwiw"
s2="iiaqewerererigotupuasdsfdjfkg"

# Method 1
a=list(set(s1)&set(s2))
print(a)

# Method 2
s3=[]
for char in set(s1):
    if char in s2:
        s3.append(char)
    else:
        continue
print(s3)