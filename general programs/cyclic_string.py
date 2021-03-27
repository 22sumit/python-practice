"""You're given a substring s of some cyclic string. What's the length of the smallest possible string
that can be concatenated to itself many times to obtain this cyclic string?
In this case "cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained by concatenating "abc" to itself. Thus, the answer is 3.
"aadddaaa"	returns 6
"ababa"	returns 2
"""

s = "aadddaaa"
temp=""
l=[]
x=""
for i in s:
    if i not in l:
        l.append(i)
    else:
        x=""+l[0]
        l.pop(0)
print(x)


