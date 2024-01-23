#OOPS (Object-Oriented Programming Language):-

class Person:
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age

    def my_detail(self):
        print("My name is ",self.name)
        print("My age is ",self.age)
        if(self.age>=18):
            print("Eligible for voting")
        else:
            print("Not Eligible for voting")
            
obj1=Person("Ahamed",23)
obj1.my_detail()


obj2=Person("Ravi",16)
obj2.my_detail()

obj3=Person("Leela",18)
obj3.my_detail()
