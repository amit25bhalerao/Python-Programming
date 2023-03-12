string = input("Enter Your String: ")

letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

for i in range(len(string)):
    if string[i].isdigit():
        digit_count += 1
    elif string[i].isupper():
        uppercase_count += 1
    elif string[i].islower():
        lowercase_count += 1

letter_count = lowercase_count + uppercase_count

dictionary = {'Letter': letter_count, 'Digit': digit_count, 'UpperCase': uppercase_count, 'Lowercase': lowercase_count}
print(dictionary)