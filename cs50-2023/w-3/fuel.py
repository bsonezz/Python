def main():
    percentage = calculator()
    if percentage<=1:
        print("E")
    elif percentage>=99:
        print("F")
    else :
        print(f"{percentage}%")
def calculator():
    while True:
        try:
            divide= (input("enter x/y: "))
            x , y = divide.split("/")
            percentage = round((int(x)/int(y))*100)
            if int(x)>int(y):
                continue
            return percentage
        except (ValueError,ZeroDivisionError):
            pass
main()
