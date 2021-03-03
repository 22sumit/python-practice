from functools import reduce

l=[2,4,7,5,10,3]
m=[1,2,3,4,5,6]
f=list(filter(lambda x:x%2==0 , l))
print("filter result: ", f)

m=list(map(lambda x:x*x , l))
print("map result: ", m)

r=reduce(lambda x,y:x+y,l)
print("reduce result: ", r)

#map function to sum 2 lists
n = [1, 2, 3]
o = [4, 5, 6]
sum=list(map(lambda x,y:x+y, n,o))
print(sum)
