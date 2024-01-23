
arr=[3,2,4,3,5,3,2,4,3,2,12,8]
n=len(arr)
for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        else:
            continue
print(arr)
#[2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 8, 12]

count=1
for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]==arr[j]):
            count=count+1
            continue
        elif(arr[i]!=arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

if(count>1):
    for k in range(0,count):
        arr[k]=arr[]
print(arr)
            
            
