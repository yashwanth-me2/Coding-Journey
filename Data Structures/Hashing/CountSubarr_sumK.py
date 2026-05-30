def countsubarr(arr,k):
    n=len(arr)
    d={0:1}
    count=0
    prefix_sum=0
    for i in range(n):
        prefix_sum+=arr[i]
        count+=d.get(prefix_sum-k,0)
        d[prefix_sum]=d.get(prefix_sum,0)+1
    return count

