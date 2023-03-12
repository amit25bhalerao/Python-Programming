# Program To Check Whether The Character Entered Is A Vowel Or Character

import sys

def check(ch):
    if len(ch) > 1:
        print("Invalid Input Entered. Program Will Terminate")
        sys.exit()
    else:
        if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            print("{} Is A Vowel".format(ch))
        else:
            print("{} Is A Character Other Than Vowel".format(ch))

    return " "


ch = input("Enter A Single Character: ")
print(check(ch))