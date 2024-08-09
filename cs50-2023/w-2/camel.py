c =input("enter: ")
for i in c:
    while i.isupper():
        c=c.replace(i , "_" + i.lower())
        break
print(c)


