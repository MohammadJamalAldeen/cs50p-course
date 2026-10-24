
def main():
    print(shorten(input("write: ")))

def shorten(text):
    text = text.strip()
    shortened = ""
    for char in text:
        if char not in "aeiouAEIOU":
            shortened += char
    return shortened

if __name__ == "__main__":
    main()