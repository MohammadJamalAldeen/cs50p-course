from random import randint
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break
    except ValueError:
        continue
rand = randint(1,level)
while True:
    try:
        n = int(input("Guess: "))
        if n <= 0:
            continue
        if n == rand:
            print("Just right!")
            break
        elif n > rand:
            print("Too large!")
        else:
            print("Too small!")
    except ValueError:
        continue
