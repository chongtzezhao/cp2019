def display_pattern(n):
    arr=[]
    s="1"
    arr.append(s)
    for i in range(2, n+1):
        s=str(i)+" "+s
        arr.append(s)

    spaces =[]
    for i in range(n):
        print((n-i-1)*2*" "+arr[i])

display_pattern(20)
