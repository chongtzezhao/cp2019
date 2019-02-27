import random

n=eval(input())
random.randint(0, 1)
for i in range(n):
    string=str(random.randint(0, 1))
    for j in range(n-1):
        string+=" " + str(random.randint(0, 1))
    print(string)
        
