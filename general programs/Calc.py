class Calc:
    def __init__(self,a,b):
        self.first=a
        self.second=b

    def getData(self):
        print("getData")

    def sum(self):
        return self.first+self.second

# obj1=Calc()
# obj1.getData()
obj=Calc(10,20)
obj.getData()
s=obj.sum()
print(s)