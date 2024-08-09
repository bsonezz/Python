x=input("enter num1 symbol num2:")
a , b , c =x.split(' ')
num1 = int(a)
num2 =int(c)
if b=="+":
    y=num1 + num2
    print(float(y))
elif b=="-":
    y=num1 - num2
    print(float(y))
elif b=="*":
    y=num1 * num2
    print(float(y))
elif b=="/" and num2!=0:
    y=num1 / num2
    print(float(y))
else:
    print("error")