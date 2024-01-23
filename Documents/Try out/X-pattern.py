str1=input("Enter the input:")
n=len(str1)
for i in range(0,n):
    for j in range(0,n):
        if(j==i or j==n-i-1):
            print(str1[j],end=" ")
        else:
            print("",end=" ")
    print()
            
