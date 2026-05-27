t=int(input())
while t:
    l=list(input())
    ans=0
    for i in range(len(l)):
        if l[i]=="4":
            ans+=1
    l=[x for x in l if x!="4"]
    if len(l):
        val=True
        while val:
            x=len(l)
            temp=l[-1]
            l=[l[z] for z in range(x-1) if (int(l[z])*10+int(l[z+1]))%4!=0]
            l.append(temp)
            if len(l)==x:
                val=False
            else:
                ans+=x-len(l)
    print(ans)
    t-=1