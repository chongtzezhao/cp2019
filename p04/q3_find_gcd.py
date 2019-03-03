def gcd(m, n):
    if m%n==0:
        return n
    return gcd(n, m%n)
