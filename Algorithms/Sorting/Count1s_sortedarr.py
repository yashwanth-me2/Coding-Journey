def count1_sortbinarr(arr):
    n=len(arr)
    left=0
    right=n-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]>=1:
            right=mid-1
        else:
            left=mid+1
    return n-left