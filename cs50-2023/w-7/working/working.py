import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if time := re.search(r"^(\d+)(?::(\d*))?\s+(AM|PM) to (\d+)(?::(\d*))?\s+(AM|PM)$", s):
        hg1 = int(time.group(1))
        hg4 = int(time.group(4))
        if hg1 > 12 or hg4 > 12:
            raise ValueError

        try:
            mg2 = int(time.group(2) or 0)
            mg5 = int(time.group(5) or 0)
        except ValueError:
            raise ValueError

        if mg2 > 59 or mg5 > 59:
            raise ValueError

        apg3 = time.group(3)
        apg6 = time.group(6)

        if apg3 == "AM" and hg1 == 12:
            hg1 = 0
        elif apg3 == "PM" and hg1 != 12:
            hg1 += 12

        if apg6 == "AM" and hg4 == 12:
            hg4 = 0
        elif apg6 == "PM" and hg4 != 12:
            hg4 += 12

        return f"{hg1:02}:{mg2:02} to {hg4:02}:{mg5:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
