n=int(input())
integers = []
test_int=2
while n!=1:
    if n%test_int==0:
        integers.append(test_int)
        n/=test_int
        test_int=2
    else:
        test_int+=1

s=""
for i in range(len(integers)-1):
    s+=str(integers[i])
    s+=", "

s+=str(integers[-1])

print(s)
