#OOPS (Object-Oriented Programming Language):-

class Person:    # class creation
    
    def __init__(self,Name,Age,Gender):  # init method or construction method
        self.name=Name
        self.age=Age
        self.gender=Gender

    def my_detail(self):    # method creation
        print("My name is ",self.name)
        print("My age is ",self.age)
        print("Gender: ",self.gender)

obj=Person("Ahamed",23,"Male")
obj.my_detail()
