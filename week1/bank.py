def bank() :
    x = input("write your greeting  ")
    x = x.lower()
    x = x.strip()
    x = x.replace(",","")
    first , *last = x.split()
    if first == "hello" :
        print("$0")
    elif  first.startswith("h") and first != "hello" :
        print("$20")
    else :
        print("$100")


bank()

