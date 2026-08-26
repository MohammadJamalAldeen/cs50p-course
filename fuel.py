def main():
    t = perfect()
    if t <= 1 :
        print("E")
    elif t >= 99 :
        print("F")
    else :
        print(f"{t}%")

def perfect() :
    while True :
        try:
            x,y = input("Fraction:").split("/")
            if  int(x)  < 0 or int(y) <= 0 :
                continue
            if int(x) > int(y) :
                continue
            d =round((int(x)/int(y))*100)
        except ValueError :
            pass
        except ZeroDivisionError :
            pass
        else :
            return(d)
main()
