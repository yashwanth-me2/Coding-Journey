def func():
    x=10
    globals()['x']=20 # used to change the global variables in local blocks
    print(x)
x=40
func()
print(x)