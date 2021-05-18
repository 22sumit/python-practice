# Command line arguments in python:
# 1st argument is always the python file name
# we can refer to the passed args by referring to the 2nd element

import sys

n=len(sys.argv)
print("total no. of arguments passed: ", n)

print("Name of python script: ", sys.argv[0])

print("Arguments passed are: ")
for i in range (1,n):
    print(sys.argv[i])

sum=0

for i in range(1,n):
    sum+=int(sys.argv[i])

print("Sum of passed arguments = ", sum)