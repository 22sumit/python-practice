class A():

    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    def add(self,a,b):
        return(self.a+self.b)
    def sub(self,a,b):
        return(self.a-self.b)
    def mul(self,a,b):
        return(self.a*self.b)
    def div(self,a,b):
        return(self.a//self.b)

n1,n2=input("Enter two numbers: ").split()
a=A(n1,n2)

operation=input("Enter the operation to perform: add/sub/mul/div : ")
if operation=='add':
    x=a.add(n1,n2)
    print(x)
elif operation=='sub':
    x=a.sub(n1,n2)
    print(x)
elif operation=='mul':
    x=a.mul(n1,n2)
    print(x)
elif operation=='div':
    x=a.div(n1,n2)
    print(x)
else:
    print("Invalid operation")