# String Palindrome
s="malayalam"
print(len(s))
r=s[::-1]
print("Palindrome") if s==r else print("Non palindrome")

# Number Palindrome
# Method 1
a=12321
bs=str(a)
rb=bs[::-1]
bi=int(rb)
print("Palindrome Number") if a==bi else print("Non palindrome Number")

# Method 2
temp=a
b=0
while temp>0:
   rem=temp%10
   b=b*10+rem
   temp = temp // 10
print("Palindrome Number") if a==b else print("Non palindrome Number")
