import re
# s="this 12 is 33 iris and 43 fingis 9 isle suistis"
# p=re.compile('\d+')
# x=p.findall(s)
# print(x)

l=["abyss", "kiuabyssoff", "aburnitpor"]
m=[]
p='a...s'
for i in l:
    x=re.search(p,i)
    if x:
        print(i)