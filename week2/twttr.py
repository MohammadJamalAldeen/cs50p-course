i = input("write: ")
i = i.strip()
for c in i :
    match c :
         case  "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" |"O" |"U" :
            i = i.replace( c , "")
print(i)


i = input("write: ")
i = i.strip()
box = ""
for c in i :
    if c not in "aeiouAEIOU":
        box = box + c
print(box)






