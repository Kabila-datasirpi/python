def student_info(Name,Subject,Total,Result):
    global Final_result #to call outside the function
    Student_name=Name
    Subject_count=Subject
    Total_mark=Total
    Final_result=Result
    return Student_name  #to return the variable

nme=input("Enter name: ")
sbj=eval(input("Enter no. of subjects: "))
mrk=eval(input("Enter mark: "))
res=input("Enter result: ")

print("Details: ")
M=student_info(nme,sbj,mrk,res)
print(M)
print(Final_result) #global variable only, lovcal variable cannot be called outside function

a="Rajesh"
b=5
c=470
d="PASS"

print("Details: ")
student_info(a,b,c,d)

print("Details: ")
student_info("Mani",6,530,"PASS")
