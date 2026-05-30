def longsubarr(arr,k):
    d={}
    n=len(arr)
    prefix_sum=0
    max_len=0
    for i in range(n):
        prefix_sum+=arr[i] 
        if prefix_sum==k:
            max_len=i+1       # for min_len tkae min of min_len and i+1
        if prefix_sum-k in d:
            max_len=max(max_len,i-d.get(prefix_sum-k))  #for min_len take min
        if prefix_sum not in d:
            d[prefix_sum]=i      # for min_len just update the value of key if key is repeated(for obtaining last occurence)
    return max_len
