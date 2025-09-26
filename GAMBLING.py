import random as r
while True:
    stake=int(input())
    dice=r.randint(1,6)
    print(dice)
    if dice==stake:
        print("WIN")
    elif stake < 1 or stake > 6:
        print("impossible")
    elif dice!=stake:
        print("LOSE")
