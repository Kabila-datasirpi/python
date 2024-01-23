def student_info(Name,Subject,Total,Result):
    Student_name=Name
    Subject_count=Subject
    Total_mark=Total
    Final_result=Result
    print("Student name= ",Student_name)
    print("No.of subjects= ",Subject_count)
    print("Total mark= ",Total_mark)
    print("Result= ",Final_result)

nme=input("Enter name: ")
sbj=eval(input("Enter no. of subjects: "))
mrk=eval(input("Enter mark: "))
res=input("Enter result: ")

print("Details: ")
student_info(nme,sbj,mrk,res)

a="Rajesh"
b=5
c=470
d="PASS"

print("Details: ")
student_info(a,b,c,d)

print("Details: ")
student_info("Mani",6,530,"PASS")
