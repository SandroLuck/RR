
def calculateCost(from_lv,to_lv):
    sum=0
    for i in range(from_lv+1,to_lv):
        sum+=i
    print(sum)

calculateCost(135,400)