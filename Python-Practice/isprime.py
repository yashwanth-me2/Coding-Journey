n=int(input("Enter a number: "))
if n<=1:
    print("Not a prime")
else:
    x=2
    while x*x<=n:
        if n%x==0:
            print("Not a prime")
            break
        x+=1
    else:   # this else block is executed when inner if loop is not executed even once, that is break is not executed.
        print("It is a prime")