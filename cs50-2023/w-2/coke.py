
due = 50
while due>0 :
    print(f"Amount Due: {due}")
    coin = input("Insert coin: ")
    if coin in ["5","25","10"]:
        due-=int(coin)
    else:
        due==50
print(f"Change Owed: {abs(due)}")

