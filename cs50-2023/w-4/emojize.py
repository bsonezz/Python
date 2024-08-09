import emoji

em = input("input: ")
print(emoji.emojize(f"{em}", language="alias"), end="")
