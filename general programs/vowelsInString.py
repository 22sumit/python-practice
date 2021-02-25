s="this is a test to FIND vowels in A string"

l=[i for i in s if i in 'aeiouAEIOU']
print(l)

set1={i for i in s if i in 'aeiouAEIOU'}
print(set1)