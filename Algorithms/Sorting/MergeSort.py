def merge(left,right):
    m=len(left)
    n=len(right)
    i=0
    j=0
    temp=[]
    while i<m and j<n:
        if left[i]<=right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    while i<m:
        temp.append(left[i])
        i+=1
    while j<n:
        temp.append(right[j])
        j+=1
    return temp
    
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)


