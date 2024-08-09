def main():
     num= input("enter x/y: ")
     per= convert(num)
     print(gauge(per))
def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            percentage = round((int(x) / int(y)) * 100)
            if percentage>100:
                raise ValueError
            return percentage
        except ZeroDivisionError :
            raise
        except ValueError :
            raise

def gauge(percentage):


    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else :
        return f"{percentage}%"

if __name__ == "__main__":
    main()
