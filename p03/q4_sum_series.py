def m_series(i):
    m=0
    for n in range(1, i+1):
        m+=n/(n+1)
    return m
print("i         m(i)")
for i in range(1, 21):
    if 10<=i<=12:
        print("{0:.0f} {1:>13.4f}".format(i, m_series(i)))
    else:
        print("{0:.0f} {1:>14.4f}".format(i, m_series(i)))
