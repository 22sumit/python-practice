# default dictionary doesn't throw keyError if the key isn't found
# dictionary throws keyError if the key isn't found

from collections import defaultdict

def get_value():
    return "key not found"

d=defaultdict(get_value)
d[1]="sumit"
d[2]="kumar"
d[3]="burnwal"
print(d[5]) #prints key not found

d1={4:"anjali", 5:"kumari"}
print(d1[8])    #keyError