meal = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00}
def main() :
    total = 0
    while True :
        try :
            m = input("Item: ").lower()
        except EOFError :
            pass
            break
        if m in meal :
            total = total + meal[m]
            print(f"Total: ${total:.2f}")
        continue
main()
