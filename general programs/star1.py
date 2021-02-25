#Star
print ("Star")
for i in range(6):
    for j in range(0,i+1):
        print('*',end="")
    print("\r")


# Inverted Star
print("Inverted Star")
for i in range(6,0,-1):
    print(i*"*")

# Star Pyramid
print("Star Pyramid")
n=7
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()

# Inverted Star Pyramid
print("Inverted Star Pyramid")
n=7
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

#Right Indented Star
print("Right Indented Star")
n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))

#Right Indented Inverted Star
print("Right Indented Inverted Star")
n=5
for i in range(n):
    print(" "*(i)+"*"*(n-i))