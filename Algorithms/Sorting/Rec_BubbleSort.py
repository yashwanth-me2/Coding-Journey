def bubblesort(arr,n):
    if n==1:
        return 
    did_swap=False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            did_swap=True
    if not did_swap:
        return
    bubblesort(arr,n-1)
    