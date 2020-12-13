from functools import reduce

l=[2,4,7,5,10,3]

f=list(filter(lambda x:x%2==0 , l))
print(f)

m=list(map(lambda x:x*x , l))
print(m)

r=reduce(lambda x,y:x+y,l)
print(r)