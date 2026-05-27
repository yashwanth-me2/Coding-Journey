def all_subseq(i,arr,ans):
    if i==len(arr):
        print(ans)
        return
    ans.append(arr[i])
    all_subseq(i+1,arr,ans)
    ans.pop()
    all_subseq(i+1,arr,ans)
all_subseq(0,[1,2,3],[])