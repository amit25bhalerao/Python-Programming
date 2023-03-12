InputString = input("Enter Your String: ")
InputSubString = input("Enter The SubString Whose Presence Is To Be Found Out: ")

if InputSubString in InputString:
    print("{} Is Present In {}".format(InputSubString, InputString))
else:
    print("{} Is Not Present In {}".format(InputSubString, InputString))