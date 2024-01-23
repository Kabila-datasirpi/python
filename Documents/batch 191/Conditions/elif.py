age=eval(input("Enter the age:"))
if(age<18):
    print("Children are not eligible to enter")
elif(18<age<50):
    print("Eligible to enter")
elif(age>50):
    print("Older people are not eligible to enter")
else:
    print("Please enter valid age")
