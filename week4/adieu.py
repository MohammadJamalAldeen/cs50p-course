import inflect
engine = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break
print()
if names != []:
    print("Adieu, adieu, to" , engine.join(names))
