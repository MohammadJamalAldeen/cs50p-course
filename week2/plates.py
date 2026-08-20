def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = s.strip()
    if s[0] and s[1].isalpha() and 2 <= len(s) <= 6 :

        return(True)





main()
