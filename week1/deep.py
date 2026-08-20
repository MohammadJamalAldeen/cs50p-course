def deep() :
    x = input("write your deep question (: ")
    x = x.strip()
    x = x.lower()
    x = x.replace("-"," ")
    x = x.replace("_"," ")
    if x == "42" or x == "forty two":
        print("Yes")
    else :
        print("No")
deep()
