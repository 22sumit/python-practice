a=[80,50,100,70,10]
l=len(a)
for i in range(l):
    index=i
    for j in range(i+1,l):
        if a[index]>a[j]:
            index=j
    a[index],a[i]=a[i],a[index]
print(a)