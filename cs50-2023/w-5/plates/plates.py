def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        return True
    else:
        return False

def is_valid(s):
    if len(s)<2 or len(s)>6 or not s[:2].isalpha():
        return False
    for c in s:
        if c.isdigit():
            if c=='0' or not  s[s.index(c):].isdigit() :
                return False
            break
        return True
if __name__ == "__main__":
    main()