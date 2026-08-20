s = input("write to comvert :)   ")
s = s.strip()
for c in s:
    if c.islower() == False :
        c = c.replace(c,"_"+c)
        c = c.lower()
        print(c,end="")
    else :
        print(c,end="")
