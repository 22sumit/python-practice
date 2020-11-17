# #Star
# for i in range(0,6):
#     for j in range(0,i+1):
#         print('*',end="")
#     print("\r")


# # Inverted Star
# for i in range(6,0,-1):
#     print(i*"*")

# Star Pyramid
n=5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()