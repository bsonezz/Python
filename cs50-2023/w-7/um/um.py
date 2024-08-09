import re

def main():
    print(count(input("Text: ")))
def count(s):
    if umnum := re.findall(r"\bum\b",s, re.IGNORECASE):
        return(len(umnum))
if __name__ == "__main__":
    main()
