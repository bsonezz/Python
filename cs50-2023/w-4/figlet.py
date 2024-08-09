# http://www.figlet.org/examples.html
from sys import exit, argv
from pyfiglet import Figlet
from random import choice


f = ["-f", "--font"]
figlet = Figlet()
fontlist = figlet.getFonts()
try:
    if argv[1] in f and argv[2] in fontlist:
        figlet.setFont(font=argv[2])

    else:
        exit("invalid-")


except IndexError:
    ch = choice(fontlist)
    figlet.setFont(font=ch)

print("output:\n", figlet.renderText(input("input:")))
