def mark_sheet(roll_number, subject_count, total_marks):
    if(total_marks>=subject_count*35):
        result='PASS'
    else:
        result='FAIL'
    print("")
    print("Roll Number: ",roll_number)
    print("No. of Subjects: ",subject_count)
    print("Total marks obtained: ",total_marks)
    print("Result: ",result)
    print("")
    
n=int(input("Enter the no. of students:"))
for i in range(n):
    roll_number = input('Enter Roll Number: ')
    subject_count = int(input('Enter Subject Count: '))
    total_marks = int(input('Enter Total Marks: '))
    mark_sheet(roll_number, subject_count, total_marks)
