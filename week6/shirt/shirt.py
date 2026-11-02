from PIL import Image
from PIL import ImageOps
import sys
import os


def main():
    try:
        argv = validate_argv(sys.argv)
        entrance = Image.open(argv[1])
        shirt = Image.open("shirt.png")
        result = ImageOps.fit(entrance, shirt.size)
        result.paste(shirt, (0, 0), shirt)
        result.save(argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")
    except ValueError as e:
        sys.exit(e)


def validate_argv(argv):
    if len(argv) < 3:
        raise ValueError("Too few command-line arguments")
    if len(argv) > 3:
        raise ValueError("Too many command-line arguments")
    a = argv[1]
    b = argv[2]
    # Splitting the file path
    root_a, ext_a = os.path.splitext(a)
    root_b, ext_b = os.path.splitext(b)
    ext_b = ext_b.lower()
    ext_a = ext_a.lower()
    if not ext_b in (".jpg", ".jpeg", ".png"):
        raise ValueError("Invalid output")
    if ext_a != ext_b:
        raise ValueError("Input and output have different extensions")
    return argv


if __name__ == "__main__":
    main()
