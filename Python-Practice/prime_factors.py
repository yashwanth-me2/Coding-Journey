def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def print_prime_factors(n):
    for i in range(2,n+1):
        if isprime(i):
            x=i
            while n%x==0:
                print(i,end=" ")
                x=x*i

print_prime_factors(40)
