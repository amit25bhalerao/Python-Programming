# Program To Reverse A List Without Using Reverse Function

def create_list():
    # Press Anything Other Than Enter To Stop Accepting The Input
    ls = []

    while True:
        x = input()

        if x == "":
            break

        ls.append(x)

    print("List: ", ls)
    # Printing The Reverse Of A List By Performing Slicing Operation On The List "List[Start, Stop, Step]"
    print("Reversed List: ", ls[::-1])


create_list()