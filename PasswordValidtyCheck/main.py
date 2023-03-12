string = input("Enter Your Password To Check For It's Validity: ")

letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0
special_count = 0
string_length = 0

for i in range(len(string)):
    if string[i].isdigit():
        digit_count += 1
    elif string[i].isupper():
        uppercase_count += 1
    elif string[i].islower():
        lowercase_count += 1
    elif string[i] == '$' or string[i] == '#' or string [i] == '@':
        special_count += 1

string_length = len(string)
letter_count = lowercase_count + uppercase_count


if uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1 and special_count >= 1 and (string_length >=6 and string_length <= 16):
    print("Password Satisfies The Following Constraints On Validity Check: ")
    print("1: At least One Upper Case Character Should Be Present")
    print("2: At least One Lower Case Character Should Be Present")
    print("3: At least One Digit Should Be Present")
    print("4: At least One Character Among '$', '#' And '@' Should Be Present")
    print("5: Password Length Should Be Between 6 To 16 Characters In Total")
else:
    print("Password Does Not Satisfy The Following Constraints On Validity Check: ")
    print("1: At least One Upper Case Character Should Be Present")
    print("2: At least One Lower Case Character Should Be Present")
    print("3: At least One Digit Should Be Present")
    print("4: At least One Character Among '$', '#' And '@' Should Be Present")
    print("5: Password Length Should Be Between 6 To 16 Characters In Total")