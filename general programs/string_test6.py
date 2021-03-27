#Use enumerate to get the index of a duplicate character in a string

s="antony"
p=[]
l=list(enumerate(s))
print(l)
# l = [(0, 'b'), (1, 'e'), (2, 'n'), (3, 'd'), (4, 'e'), (5, 'd')]
print(len(l))
m=[]
for i in range (len(l)):
    x=l[i][1]*(l[i][0]+1)
    m.append(x)
n="-".join(m)
print(n)

# Wrong Method: index always returns the first position of a char
for i in s:
    p.append(i*(s.index(i)+1))
print("-".join(p))