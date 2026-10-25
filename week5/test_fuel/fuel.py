def main():
    while True:
        fraction = input("Fraction:")
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError) :
            continue
        print(gauge(percentage))
        break

def convert(fraction):
    x, y = fraction.split("/")
    if int(x) < 0 or int(y) < 0:
        raise ValueError
    if int(y) == 0:
        raise ZeroDivisionError
    if int(x) > int(y):
        raise ValueError
    return round((int(x) / int(y)) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
