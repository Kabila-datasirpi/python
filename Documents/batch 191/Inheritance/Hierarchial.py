#Hierarchial Inheritance:

class Parent:
    def test1(self):
        print("Parent class")
        
class Child1(Parent):
    def test2(self):
        print("Child class - 1")
        
class Child2(Parent):
    def test3(self):
        print("Child class - 2")

obj=Child2()
obj.test1()
obj.test3()

print("")

obj=Child1()
obj.test1()
obj.test2()
