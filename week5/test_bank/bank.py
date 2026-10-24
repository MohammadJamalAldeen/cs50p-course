def main():
    print("$",value(input("Write your greeting: ")),sep="")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return int(0)
    elif greeting.startswith("h") and greeting != "hello":
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()
