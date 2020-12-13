s="sumit"
k="sumit"
l=s
b=s+k
print(b)
print (id(s))
print (id(k))
print (id(l))
print (id(b))

# Strings are immutable, therefore, whenever it is concatenated,
#   it is assigned to a new variable (new memory location).
# If 2 strings are having same value then the refer to the same memory location.