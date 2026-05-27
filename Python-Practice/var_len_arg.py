def printdetails(id,**kwargs):
    print("Details of",id,":")
    for d,v in kwargs.items():
        print(d,"is",v)
def add(init_sum,*posargs):
    x=sum(posargs)
    return init_sum+x

printdetails(100,name="car",color="black")
y=add(12,6,7,8,9)
print(y)