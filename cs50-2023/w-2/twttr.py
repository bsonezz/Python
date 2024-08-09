exp = input("enter: ")
for i in exp:
    while i in ['A','a','E','e','I','i','O','o','U','u']:
        exp= exp.replace(i, '')
        break
print(exp)