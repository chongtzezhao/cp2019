side = [0,0,0]
for i in range(3):
    j=str(i+1)
    side[i]=eval(input(f"Enter side {j}: "))
    
if side[0]+side[1]<=side[2] or side[2]+side[1]<=side[0] or side[0]+side[2]<=side[1]:
    print("Invalid triangle!")
else:
    print(side[0]+side[1]+side[2])
