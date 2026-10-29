import csv
import sys
from tabulate import tabulate


def main():
    try:
        path = get_path(sys.argv)
        table = reading(path)
    except FileNotFoundError:
        sys.exit("File does not exist")
    except ValueError as e:
        sys.exit(e)

    print(tabulate(table, headers="keys", tablefmt="grid"))


def get_path(argument):
    if len(argument) < 2:
        raise ValueError("Too few command-line arguments")
    if len(argument) > 2:
        raise ValueError("Too many command-line arguments")
    if not argument[1].endswith(".csv"):
        raise ValueError("Not a CSV file")

    return argument[1]


def reading(path):
    with open(path) as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    main()
