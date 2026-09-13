d={}
def main() :
    while True:
        try:
            items = input().upper().strip()
            d[items] = d.get(items,0) + 1
        except EOFError :
                break
    for items in sorted(d) :
        print(d[items],items)
main()

