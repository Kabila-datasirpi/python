n=int(input("Enter the number")) #10
n=n-2
num1=0
num2=1
num3=num2 #1
sum=1
print(num1,num2,end=" ")
while(sum<=n):          #(1<10 #2<10 #3<10...)
    print(num3,end=" ") #(1 #2 #3...)
    sum+=1              #(1+1=2   #2+1=3  #3+1=4....)
    num1=num2           #(num1=1  #num1=1 #num1=2....)
    num2=num3           #(num2=1  #num2=2 #num2=3....)
    num3=num1+num2      #(num3=1+1=2 #num3=1+2=3 #num3=2+3=5....)
print()        
        
#0,1,1,2,3,5,8,13.
