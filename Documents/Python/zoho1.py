n=int(input("Enter the no. of elements:"))
arr=[]
for i in range(0,n):
    elem=int(input("Enter the elements:"))
    arr.append(elem)
print(arr)
for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        else:
            continue
print(arr)
print("The largest elements are:",arr[n-1],arr[n-2])
