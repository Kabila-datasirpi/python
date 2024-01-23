arr=[3,5,6,2,8,9,10,13,7]
l=len(arr)
for i in range(0,l):
    for j in range(i+1,l):
        if(arr[i]<arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        else:
            continue
print("The Descending sorted array is ",arr)
