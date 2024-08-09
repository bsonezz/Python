import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("few")
    elif len(sys.argv) > 2:
        sys.exit("many")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("not python file")
        else:
            print(lines(sys.argv[1]))


def lines(file):
    try:
        counter = 0
        with open(file, "r") as f:
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    counter = counter + 1
                return counter
    except FileNotFoundError:
        sys.exit("no exist")


if __name__ == "__main__":
    main()
