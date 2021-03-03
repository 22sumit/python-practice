def adder(**x):
    print(x)

def add(*x):
    print("sum: ", sum(x) )

add(5,10,15,20,25)
adder(name="sumit")