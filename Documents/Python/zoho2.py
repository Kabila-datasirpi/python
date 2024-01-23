
def sorting(arr):
    freq={}
    for i in arr:
        if(i in freq):
            freq[i]+=1
        else:
            freq[i]=1

    sorted_array=sorted(arr,key=lambda x:(-freq[x],x))
    return sorted_array

arr=[3,2,4,3,5,3,2,4,3,2,12,8]
op_arr=sorting(arr)
print(op_arr)
