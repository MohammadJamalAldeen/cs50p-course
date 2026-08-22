def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6) :
        return(False)
    if not (s[0].isalpha() and s[1].isalpha() and  s.isalnum() ):
        return(False)
    num = False
    zero = False
    for c in s :
        if c == "0" and not num :
            zero = True
        if c.isdigit()  :
            num = True
        if zero  and num :
            return(False)
        if not c.isdigit()  and num  :
            return(False)
    return(True)
main()
# num vs zero: a rivalry for the ages.
