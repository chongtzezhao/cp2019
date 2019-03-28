x,y=input().split(" ")
num=int(input())

counter=0
payments={"A":4,"K":3,"Q":2,"J":1}
center=""
curr_player="x"
deal=False
dealer=""

while counter!=num:
    if curr_player=="x":
        center=center+x[0]
        target=x[0]
        x=x[1:]
        curr_player="y"
        dealer="y"
    else:
        center=center+y[0]
        target=y[0]
        y=y[1:]
        curr_player="x"
        dealer="x"
    if target=="A" or target=="K" or target=="Q" or target=="J":
        #complete payment, find curr_player
        i=0
        end_deal=False
        x_deal=0
        y_deal=0
        while not end_deal:
            if dealer=="x":
                center=center+x[0]
                x_deal+=1
                if x[0]=="A" or x[0]=="Q" or x[0]=="K" or x[0]=="J":
                    dealer="y"
                    target=x[0]
                    x_deal=0
                if x_deal==payments[target]:
                    end_deal=True
                x=x[1:]
            if dealer=="y":
                center=center+y[0]
                y_deal+=1
                if y[0]=="A" or y[0]=="Q" or y[0]=="K" or y[0]=="J":
                    dealer="x"
                    target=y[0]
                    y_deal=0
                if y_deal==payments[target]:
                    end_deal=True
                y=y[1:]
        counter+=1
        if dealer=="x":
            curr_player="y"
            y=y+center
            center=""
        else:
            curr_player="x"
            x=x+center
            center=""
print(x)
#79A6K334
