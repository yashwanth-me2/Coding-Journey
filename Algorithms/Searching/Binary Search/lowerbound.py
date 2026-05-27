def lowerbound(arr,x):
    s=0,e=len(arr)-1
    ans=len(arr)
    while s<=e:
        mid=s+(e-s)//2
        if arr[mid]>=x:
            ans=mid
            e=mid-1
        else:
            s=mid+1
    return ans