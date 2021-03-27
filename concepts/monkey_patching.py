'''Modify the behavior of a function at runtime.
In order to modify the test data that we are already using without changing the code.'''

class Monkey():

    def get_data(self):
        print("taking data from db")

def new_get_data(self):
    print("taking data from new source")

Monkey.get_data=new_get_data
#new_get_data is not the object but a reference of it.
#So we haven't used parenthesis after the function name.

m1=Monkey()
m1.get_data()
