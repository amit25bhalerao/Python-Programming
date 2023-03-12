def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


text = input("Enter The Input String: ")
s = int(input("Enter The Shift Value: "))

print("Plain Text: " + text)
print("Shift Value : " + str(s))
print("Cipher: " + encrypt(text, s))