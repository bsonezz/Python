from random import randint


def main():
    score = generate_integer(get_level())


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except:
            pass


def generate_integer(level):
    score = 0
    for i in range(10):
        time = 0

        if level == 1:
            x = randint(0, 9)
            y = randint(0, 9)
        elif level == 2:
            x = randint(10, 99)
            y = randint(10, 99)
        elif level == 3:
            x = randint(100, 999)
            y = randint(100, 999)

        while time < 3:
            try:
                sum = int(input(f"{x} + {y} = "))
                if sum == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    time += 1
                    if time == 3:
                        print(f"{x} + {y} = {x + y}")
            except:
                print("EEE")
                time += 1
                if time == 3:
                    print(f"{x} + {y} = {x + y}")

    print("Score:", score)


if __name__ == "__main__":
    main()
