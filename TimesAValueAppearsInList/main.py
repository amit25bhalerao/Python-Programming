# Value Count

def create_list(ls):
    # Press Anything Other Than Enter To Stop Accepting The Input

    while True:
        x = input()

        if x == "":
            break

        ls.append(x)

    return ls

def count_value(ls, se):
    count = 0
    for x in ls:
        if x == se:
            count += 1

    print(se, "Appeared For ", count, " Times In ", ls)


ls = []
ls = create_list(ls)

se = input("Enter The Search Element: ")
count_value(ls, se)
