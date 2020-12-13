class myExc(Exception):
    def __init__(self,message):
        super().__init__(message)

n=int(input("Enter a number: "))

if n>10:
    print("Excellent")
elif n<10:
    raise myExc("Enter a larger number")
