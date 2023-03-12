String = input("Enter The String: ")
Word = ''
MaxLen = 0
MaxWord = ''

for i in String + ' ':
    if i == ' ':
        if len(Word) > MaxLen:
            MaxWord = Word
        Word = ''
    else:
        Word += i


print("Longest Word: ", MaxWord)
print("Length: ", len(MaxWord))