def func(i,sum,arr):
    if sum==0:
        return True
    elif sum<0 or i==len(arr):
        return False
    return func(i+1,sum-arr[i],arr) + func(i+1,sum,arr)  #for just checking  any susbsequence with given sum, replace '+' with 'or' 

def subseq_sum(arr,sum):
    return func(0,sum,arr)

print(subseq_sum([4,2,10,5,1,3],5))