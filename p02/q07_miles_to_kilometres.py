print("Miles Kilometres Kilometres Miles")
for i in range(1, 11):
    if 7<=i<=9:
        print(i, "{0:>10.3f} {1:>6.0f} {2:>14.3f}".format(i*1.609, 5*i+15, (5*i+15)*1/1.609))
    elif i==10:
        print(i, "{0:>9.3f} {1:>6.0f} {2:>14.3f}".format(i*1.609, 5*i+15, (5*i+15)*1/1.609))
    else:
        print(i, "{0:>9.3f} {1:>7.0f} {2:>14.3f}".format(i*1.609, 5*i+15, (5*i+15)*1/1.609))
  #  print(i, "{0:>9.3f} {1:.0f} {2:.3f}".format(i*1.609, 5*i+15, (5*i+15)*1.609))
