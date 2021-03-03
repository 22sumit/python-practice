l=[1,2,3,4,5,6,7,8]

lc=[x*x for x in l]
print(lc)

# Example: finding vowels in a string
s="this is a test to find all the vowels in this string"
vowels1={i for i in s if i in 'aeiou'}
print(vowels1)

vowels2=[i for i in set(s) if i in 'aeiou']
print(vowels2)