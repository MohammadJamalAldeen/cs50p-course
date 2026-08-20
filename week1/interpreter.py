def interpreter() :
    a = input("Write arithmetic expression ")
    x , y , z = a.split()
    x = int(x)
    z = int(z)
    y = y.strip()
    if y == "+" :
        print(float(x+z))
    elif y == "-" :
        print(float(x-z))
    elif y == "*" :
            print(float(x*z))
    elif y == "/" :
        print(float(x/z))
interpreter()

