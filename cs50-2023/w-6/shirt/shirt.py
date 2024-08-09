import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv)<3:
        sys.exit("too few command line")
    elif len(sys.argv)>3:
        sys.exit("too mnay command line")
    else:
        format = [".jpg",".png",".jpeg"]
        input = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        if output[1].lower() not in format:
            sys.exit("Invalid Output")
        elif input[1].lower()!= output[1].lower():
            sys.exit("diffrent extesions ")
        else:
            shirt(sys.argv[1],sys.argv[2])


def shirt(inp,out):
    try:
        tshirt= Image.open("shirt.png")
        with Image.open(inp) as inp:
            edit = ImageOps.fit(inp,tshirt.size)
            edit.paste( tshirt, mask=tshirt)
            edit.save(out)
    except FileNotFoundError:
        sys.exit("not exist")
if __name__ == "__main__":
    main()


