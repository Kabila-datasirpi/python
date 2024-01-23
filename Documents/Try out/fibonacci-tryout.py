n=int(input("Enter:"))
n=n-2
num1=0
num2=1
num3=num2
sum=0
print(num1,num2,end=" ")
for i in range(n+1):
    print(num3,end=" ")
    sum+=i
    num1=num2
    num2=num3
    num3=num1+num2
print()
    
