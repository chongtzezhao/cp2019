def is_prime(n):
    if n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3, int(n**(1/2))+1, 2):
        if n%i==0:
            return False
    return True

rows=0
check=2
while rows<100:
    string=""
    primes=0
    while primes<10:
        while is_prime(check)==False:
            check+=1
        string+=str(check) + " "
        check+=1
        primes+=1
    print(string)
    rows+=1


'''check=3
while is_prime(check)==False:
    if is_prime(check):
        print(check)
        check+=1
    else:
        check+=1'''

print(check)
