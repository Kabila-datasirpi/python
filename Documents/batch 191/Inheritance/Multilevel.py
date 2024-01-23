#Multilevel Inheritance:   (more than one child class)

class Parent:
    def test1(self):
        print("Parent class")
        
class Child1(Parent):
    def test2(self):
        print("Child class 1")
        
class Child2(Child1):
    def test3(self):
        print("Child class 2")
        
obj=Child2()
obj.test1()
obj.test2()
obj.test3()
