n=int(input("Enter the number:"))
factorial=1
if(n>0):
    for i in range(1,n+1):
        factorial*=i
    print("The factorial is ",factorial)
else:
    print("Invalid input")
        
