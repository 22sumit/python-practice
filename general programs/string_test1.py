"""Write a function that takes a string input, and returns the first character that is
not repeated anywhere in the string. Characters in strings consist of printable characters.
As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter.
For example, the input 'sTreSS' should return 'T'."""

str="sTreSs"
l=[i for i in set(str) if str.count(i)==1]
print(l)

ind=[]
for c in l:
    if str.lower().count(c.lower())==1:
        ind.append(str.index(c))
if len(ind):
    print("First occuring single character: ",str[min(ind)])
else:
    print("No single chars in provided string")