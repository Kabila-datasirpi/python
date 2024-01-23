x=int(input("Enter the number:"))
for i in range(1,x+1):
    for j in range(x-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
