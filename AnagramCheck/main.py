# A Program To Check Whether Two Strings Are Anagram Or Not

def anagramcheck(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

str1 = input("Enter The First String: ")
str2 = input("Enter The Second String: ")
print(anagramcheck(str1, str2))
