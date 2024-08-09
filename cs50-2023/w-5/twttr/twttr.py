
def main():
    w= input("Enter a word: ")
    print(shorten(w))

def shorten(word):
    final=""
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    for i in word:
        if i not in vowels:
            final+=i
    return final

if __name__ == "__main__":
    main()
