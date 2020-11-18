mystr = "I love my India"

list = mystr.split(' ')
new_str=""
for item in list:
    new_str +=item[::-1] +" "

print (new_str.strip())

rev=mystr[::-1]
print (rev)

list1=mystr.split(" ")
str2=""
for word in list1:
    str2=" "+word+str2
print (str2.strip())