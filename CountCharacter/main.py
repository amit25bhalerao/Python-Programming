# Program To Count The Number Of Vowels In A Given String

def check(string, ch):
    count = 0
    for i in string:
        if i == ch:
            count += 1
    print("Number Of Occurrences Of ", ch, "Is/Are ", count)

string=input("Enter The String:")
ch = input("Enter Your Desired Character: ")

check(string,ch)

