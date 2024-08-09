import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv)<2:
        sys.exit("few")
    elif len(sys.argv)>2:
        sys.exit("many")
    else:
        if sys.argv[1][-4:]!= ".csv":
            sys.exit("not file")
        else:
            print(tabulize(sys.argv[1]))

def tabulize(file):
    try:
        with open(file) as f:
            reader = csv.reader(f)
            table= tabulate(reader, headers="firstrow", tablefmt="grid")
            return table

    except FileNotFoundError:
        sys.exit("not found")

if __name__ == "__main__":
    main()