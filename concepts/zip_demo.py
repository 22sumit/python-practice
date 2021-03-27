month = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Sep', 'Oct', 'Nov', 'Dec']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res={month[i]:num[i] for i in range(len(month))}
print(res)
print(type(res))

z=zip(month, num)
z1=list(zip(month,num)) #returns a list of tuples
print(z) #returns a zip object
print(dict(z))  #returns a dictionary
print(z1)   #returns a list of tuples

'''
zip function returns an iterator capable of producing tuples.
It can be applied to all iterable objects like lists, tuples, strings, dictionaries, sets, range.
Can be used to pack and unpack lists.
use the star operator to unpack the list. See example below.'''

cities_and_population = [("Zurich", 415367), ("Geneva", 201818), ("Basel", 177654), ("Lausanne", 139111)]

city,population=zip(*cities_and_population)
print(city)
print(population)