from random import randint

while True:
    try:
        max = int(input("Level: "))
        if max >= 0:
            rand = randint(1, max)
            break

        else:
            continue

    except ValueError:
        continue
while True:
    try:
        guess = int(input("Guess: "))
        if guess >= 1 and guess <= max:
            if guess == rand:
                print("Just right!")
                break
            elif guess > rand:
                print("Too large!")
            else:
                print("Too small!")

        else:
            pass

    except ValueError:
        pass
