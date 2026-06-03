def freq_extremes(arr):
    if not arr:
        return None
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    return max(d.values()),min(d.values())