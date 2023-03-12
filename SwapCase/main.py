def swap_case(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result


string = input("Enter The String: ")
print(swap_case(string))