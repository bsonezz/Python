months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    unformatted =input("enter: ").title()
    try:
        m , d, y =unformatted.split('/')
        m =int(m)
        d= int(d)
        y = int(y)
        if 1<=d<=31 and 1<=m<=12 and 1000<=y<=9999:
            print(f"{y}-{m:02}-{d:02}")
            break
    except :
        try:
            md , y =unformatted.split(',')
            m ,d = md.split(" ")
            d= int(d)
            y= int(y)
            if m in months and 1<=d<=31  and 1000<=y<=9999:
                m =int(months.index(m)+1)
                print(f"{y}-{m:02}-{d:02}")
                break
        except :
            pass

