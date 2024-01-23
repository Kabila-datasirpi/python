n=int(input("Enter the number")) #10
n=n-2
num1=0
num2=1
num3=num2 #1
sum=0
print(num1,num2,end=" ")
for i in range(1,n+1):          
    print(num3,end=" ") 
    sum+=i              
    num1=num2           
    num2=num3           
    num3=num1+num2      
print()  
