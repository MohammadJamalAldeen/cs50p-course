import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.fullmatch(r"([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)", s):
        start_h = matches.group(1)
        start_m = matches.group(2)
        start_period = matches.group(3)
        end_h = matches.group(4)
        end_m = matches.group(5)
        end_period = matches.group(6)
        start_h = int(start_h)
        end_h = int(end_h)

        if start_h != 12 and start_period == "PM":
            start_h += 12
        if end_h != 12 and end_period == "PM":
            end_h += 12
        if start_h == 12 and start_period == "AM":
            start_h = 0
        if end_h == 12 and end_period == "AM":
            end_h = 0

        if start_m is None:
            start_m = 0
        if end_m is None:
            end_m = 0
        start_m = int(start_m)
        end_m = int(end_m)

        return f"{start_h:02}:{start_m:02} to {end_h:02}:{end_m:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
