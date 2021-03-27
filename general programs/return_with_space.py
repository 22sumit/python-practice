#Given a list of integers return the min and max value as a string separated by space
def operation(s):
    # m=[int(i) for i in s.split(" ")]
    l=list(map(int, s.split(" ")))
    print("l: ",l)
    length= len(l)
    for i in range(length-1):
        for j in range (length-i-1):
            if l[j]<l[j+1]:
                l[j+1],l[j]=l[j],l[j+1]
    print(l)
    ss=str(l[0])
    ms=str(l[length-1])
    new=ss+" "+ms
    print("variable \"new\" is of type:", type(new))
    return (new)

x=operation("70 80 50 100 20")
print(x)