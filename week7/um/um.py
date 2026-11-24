import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b",s,re.IGNORECASE)
    um_num = len(matches)
    if um_num > 0:
        return  um_num
    else:
        return 0

if __name__ == "__main__":
    main()
