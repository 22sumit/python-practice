import random

# randon int between 1 and 10
x= random.randint(1, 10)
print(x)

#random float between 0 and 1
y=random.random()
print(y)

#random float between 1 and 10
z=random.uniform(1,10)
print(z)

# choose a random value from the list
mylist=list("ABCDEFGHIJ")
a=random.choice(mylist)
print(a)
# choose n random values from the list
b=random.sample(mylist, 3)
print(b)

#shuffle a list
random.shuffle(mylist)
print(mylist)
