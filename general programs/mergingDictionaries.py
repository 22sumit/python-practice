x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}

#Method 1
z={**x, **y}
print(z)

#Method 2
d=x.copy()
d.update(y)
print(d)

x.update(y)
print(x)
'''
In python 3.9 this can be done simply by:
d1 = x | y  
'''