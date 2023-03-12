# Python program to find smallest number from list

def create_list(ls):
    # Press Anything Other Than Enter To Stop Accepting The Input

    while True:
        x = input()

        if x == "":
            break

        ls.append(x)

    return ls

def minimum(ls):
    print("Minimum Value: ", min(ls))

ls = []
ls = create_list(ls)
minimum(ls)
