import inflect

namelist = []
while True:
    p = inflect.engine()
    try:
        name = input("names: ")
        namelist.append(name)  # appendix and adding to list

    except EOFError:
        break
print("Adieu, adieu, to " + p.join(namelist))
