import csv
import sys


def main():
    try:
        argv = validate_argv(sys.argv)
        with open(argv[1], newline="") as infile:
            reader = csv.DictReader(infile)
            students = reformat_students(reader)
            write_students(students, argv)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    except ValueError as error:
        sys.exit(error)


def validate_argv(argv):
    if len(argv) < 3:
        raise ValueError("Too few command-line arguments")
    if len(argv) > 3:
        raise ValueError("Too many command-line arguments")

    return argv


def reformat_students(rows):
    students = []
    for row in rows:
        last, first = row["name"].split(",")
        first = first.strip()
        house = row["house"]
        students.append({"first": first, "last": last, "house": house})
    return students


def write_students(students, argv):
    with open(argv[2], "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
