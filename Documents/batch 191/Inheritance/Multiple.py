#Multiple Inheritance: (more than one parent class)

class Parent1:
    def test1(self):
        print("Parent class 1")
        
class Parent2:
    def test2(self):
        print("Parent class 2")
        
class Child(Parent1,Parent2):
    def test3(self):
        print("This is child class")

obj=Child()
obj.test1()
obj.test2()
obj.test3()
