print("Kilograms Pounds")
for i in range(1, 11):
    if 5<=i<=9:
        print(i, "{0:>12.1f}".format(i*2.2))
    else:
        print(i, "{0:>11.1f}".format(i*2.2))
    
