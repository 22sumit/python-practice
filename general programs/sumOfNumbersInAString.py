n = input("Enter an Alpha-Numeric String: ")
sum = 0
temp = ""
for i in n:
    if (i.isalpha()):
        if (temp != ""):
            sum = sum + int(temp)
            temp = ""
    else:
        temp = str(temp) + str(i)

if (temp != ""):
    sum = sum + int(temp)
    temp = 0

print(sum)