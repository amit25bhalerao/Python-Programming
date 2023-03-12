InputString = input("Enter The Input String: ")
Word = InputString.split(' ')
Word = list(reversed(Word))
print("Output String: ", " ".join(Word))