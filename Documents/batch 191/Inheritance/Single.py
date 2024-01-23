#Single Inheritance:

class Parent:
    def __init__(self,Laptop,Price):
        self.laptop=Laptop
        self.price=Price
        
    def func1(self):
        print("Laptop brand is ",self.laptop)
        print("Laptop price is ",self.price)
        
class Child(Parent):
    def func2(self):
        print("All parent details are inherited in this child class")
        
obj=Child("HP",40000)
obj.func1()
obj.func2()

obj2=Child("Lenovo",38000)
obj2.func1()
obj2.func2()

obj3=Child("Dell",50000)
obj3.func1()
obj3.func2()
        
        
