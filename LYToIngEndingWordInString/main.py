String = input("Enter The String: ")
NewString = ''

Last3Characters = String[(len(String)-3): (len(String)+1)]
print("Last 3 Characters Of Given String: ", Last3Characters)

if Last3Characters == 'ing' and len(String) >= 3:
    NewString = String + 'ly'
elif Last3Characters != 'ing' and len(String) >= 3:
    NewString = String + 'ing'
elif len(String) < 3:
    NewString = String


print("Original String: ", String)
print("New String: ", NewString)