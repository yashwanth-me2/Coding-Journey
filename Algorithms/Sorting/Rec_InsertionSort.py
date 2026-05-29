def insertionsort(arr,i,n):
    if i==n-1:
        return
    j=i
    temp=arr[j+1]
    while j>=0 and arr[j]>temp:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
    insertionsort(arr,i+1,n)
arr=[2,9,7,6,0,1,3]
insertionsort(arr,0,7)
print(arr)