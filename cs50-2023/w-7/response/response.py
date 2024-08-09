from validator_collection import checkers

email = input("email: ")
if checkers.is_email(email):
    print("Valid")
else:
    print ("Invalid")