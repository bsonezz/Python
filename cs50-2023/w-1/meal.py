
def main():
    hour = input("the time: ")
    time = convert(hour)
    if 7.00<= time <=8.00:
        print("breakfast time")
    elif 12.00<=time<=13.00:
        print("lunch time")
    elif 18.00<=time<=19.00:
        print("dinner time")
def convert(hour):
    if "a.m." in hour or "p.m."in hour:
        time1 , pm = hour .split(" ")
        hour , minute = time1.split(":")
        if pm=="p.m." and  int(hour)!=12:
            hour = int(hour)+12
        elif pm=="a.m." and int(hour)==12:
            hour = False

    else:
        hour , minute = hour .split (":")

    hour = float(hour) + (float(minute)/60)
    return hour

if __name__ == "__main__":
    main()


