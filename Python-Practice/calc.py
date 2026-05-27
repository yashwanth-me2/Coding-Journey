import sys
print('''
Enter the choice number of arithmetic operation from below:
1 -> Addition
2 -> Subtraciton
3 -> Multiplication
4 -> Division(Float division)
5 -> Power operator
''')
choice=int(input("Choice="))
if choice not in (1,2,3,4,5):
    print("--- Invalid Operator ---")
    sys.exit()
a=int(input("\nEnter first number:"))
b=int(input("Enter second number:"))

print("Result is: ",end="")
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print(a**b)