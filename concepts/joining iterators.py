l1 = ['Jan', 'Feb', 'Mar', 'Apr']
l2 = [1, 2, 3, 4]
l3 = [9,8,7,6]

l1.extend(l2)   #add the new list to existing list
print("l1 extend: ",l1)
l4=l3+l2    #creates a new list and adds two lists in new list
print("l4 +: ",l4)
l4.append(100)
print("l4 append: ",l4)

s1={1,2,3,4}
s2={5,6,7}
s3={8,9,10,11,12}
s4=s1.union(s2) #creates a new set and adds two sets in the new set
print("s4 union: ",s4)
s3.update(s2)   #adds a new set to the existing set
print("s3 update: ",s3)
s3.add(100) # Adds a new element to the set
print("s3 add: ",s3)

#tuples are unchangeable. so to add elements to a tuple: tuple->list->modify->list->tuple

d1={'a':1,'b':2,'c':3}
d2={'c':4,'d':5}
d3={'e':6,'f':7}
d1.update(d2)   # Updates the existing dictionary and any values that has a matching key in both dicts.
print("d1 update: ",d1)
d4={**d2, **d3} #joining two dictionaries using keyword argument **kwargs
print("d4: **",d4)
