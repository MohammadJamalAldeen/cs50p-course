total = 0
while total < 50 :
    c = int(input("Insert Coin: "))
    if c in (5 , 10 , 25):
        total = total + c
        if total < 50 :
            print("Amount Due:", 50 - total)
        else :
            print("Change Owed:", total - 50)
    else :
        print("Amount Due:", 50 - total)













