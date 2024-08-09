greet = input("say welcome: ").strip().lower()

if "hello" in greet:
    print("$0")
elif greet[0]=="h":
#elif greet.find('h',0,1)==0:
    print("$20")
else:
    print("$100")