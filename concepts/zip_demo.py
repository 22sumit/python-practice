l1=[1,2,3,4,5,6]
l2=['a','b','c','d']
z=zip(l1,l2)
print(z) #returns a zip object

print(list(z))  #returns a list of tuples

'''
zip function returns an iterator capable of producing tuples.
It can be applied to all iterable objects like lists, tuples, strings, dictionaries, sets, range.
Can be used to pack and unpack lists.
use the star operator to unpack the list. See example below'''

cities_and_population = [("Zurich", 415367),
                         ("Geneva", 201818),
                         ("Basel", 177654),
                         ("Lausanne", 139111),
                         ("Bern", 133883),
                         ("Winterthur", 111851)]

city,population=zip(*cities_and_population)
print(city)
print(population)