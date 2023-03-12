string = input("Enter Your String: ")

letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0
space_count = 0

for i in range(len(string)):
    if string[i].isdigit():
        digit_count += 1
    elif string[i].isupper():
        uppercase_count += 1
    elif string[i].islower():
        lowercase_count += 1
    elif string[i].isspace():
        space_count += 1

letter_count = lowercase_count + uppercase_count


print("Digit Count: ", digit_count)
print("Upper Case Count: ", uppercase_count)
print("Lower Case Count: ", lowercase_count)
print("Space Count: ", space_count)
print("Letter Count: ", letter_count)