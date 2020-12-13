a=[80,50,100,70,10]
l=len(a)
for i in range(l-1):
    for j in range(0,l-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)