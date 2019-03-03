def reverse_int(n):
    n=str(n)
    if len(n)==1:
        return n
    else:
        return n[-1] + reverse_int(n[:-1])
