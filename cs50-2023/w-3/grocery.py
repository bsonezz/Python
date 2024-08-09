
counter = {}

while True:
    try:
        fruit = str(input("")).upper()
        if fruit in counter:
            counter[fruit] += 1
        else:
            counter[fruit] = 1
    except EOFError:
        break

sorted = sorted(counter.items())

for fruit, number in sorted:
    print(f"{number} {fruit}")