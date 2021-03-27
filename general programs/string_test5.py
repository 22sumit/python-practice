# Check if a string can be split into substrings starting with digit N followed by N characters

s = "4g12y6hunter"
c=j=0
for i in range (j, len(s)):
    if j<len(s):
        i=j
        if s[i].isdigit():
            t=s[i+1:i+int(s[i])+1]
            if len(t)==int(s[i]):
                c=0
                j=i+int(s[i])+1
            else:
                c=1
                break
print("string cannot be split into substrings") if c==1 else print("string can be split into substrings")