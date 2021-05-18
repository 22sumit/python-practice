# Method 1
# with open("../resources/test1.txt") as f:
#     line=f.readline()
#     while line!="":
#         print(line)
#         line=f.readline()
#     print("end of file !!")

# Method 2
with open("../resources/test1.txt","r") as f1:
    for line in f1.readlines():
        print(line)

#Reverse file contents and write back to file
with open("../resources/test1.txt","r") as f2:
    content=f2.readlines()
    reversed(content)
with open("../resources/test1.txt","w") as f3:
    for line in reversed(content):
        f3.write(line)
