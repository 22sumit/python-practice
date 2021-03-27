"""
Program to check if strings are rotations of each other or not
"""

s1="ABACD"
s2="CDABA"
temp=s1+s1
if temp.count(s2)>0:
    print("rotations")
else:
    print("not rotations")
