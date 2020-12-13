l=[50,20,100,80,30]
length=len(l)
for i in range(length-1):
    for j in range(i+1,length):
        if (l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
print(l)
print("2nd largest number : ", l[length-2])