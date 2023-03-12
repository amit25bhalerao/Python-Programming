String = input("Enter The String: ")

NewString = FirstCharacter = String[0]

print("Original String: ", String)

for i in range(1, len(String)):
    if String[i] == FirstCharacter:
        NewString += '$'
    else:
        NewString += String[i]


print("Result String: ", NewString)
