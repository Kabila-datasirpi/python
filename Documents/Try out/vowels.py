string=input("Enter the input:")
string=string.lower()
count=0
for i in string:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" in string):
        print("The vowels are:",i)
        count+=1
print("No.of vowels = ",count)
