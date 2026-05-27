def pow(x,n):
    if n<0:
        n=-n
        x=1/x
    if n==0:
        return 1
    ans=1
    while n:
        if n%2!=0:
            ans=x*ans
        x=x*x
        n=n//2
    return ans
print(pow(3,4))