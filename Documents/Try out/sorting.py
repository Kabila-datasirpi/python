arr=[3,5,6,2,8,9,10,13,7]
arr1=len(arr)
for i in range(0,arr1):
    for j in range(i+1,arr1):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        else:
            continue
print("The Ascending sorted array is ",arr)
print("the smallest 2 numbers are",arr[0],arr[1])
print("the largeest 2 numbers are",arr[arr1-1],arr[arr1-2])
