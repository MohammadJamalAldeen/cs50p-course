i = input("write: ")
i = i.strip()
box = ""
for c in i :
    if c not in "aeiouAEIOU":
        box = box + c
print(box)
