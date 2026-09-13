months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date :
                month, day, year = date.replace("/", " ").split()
            elif "," in date :
                month, day, year = date.replace(",", " ").split()
                month = months.index(month) + 1
            else:
                continue
            month, day, year = int(month), int(day), int(year)
            if year > 0 and 0 < day < 32 and 0 < month < 13:
                print(f"{year:04}-{month:02}-{day:02}")
                break
            else:
                    continue
        except ValueError :
            continue
main()
