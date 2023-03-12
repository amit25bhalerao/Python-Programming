def create_list(ls):

    print("Enter 10 Values Into The List")
    while True:
        x = int(input())

        if len(ls) == 9:
            break

        ls.append(x)

    return ls

def even_odd_lists(ls):
    ls_odd = []
    ls_even = []

    for i in ls:
        if i % 2 != 0:
            ls_odd.append(i)
        else:
            ls_even.append(i)

    print("Odd_List: ", ls_odd)
    print("Even_List; ", ls_even)

ls = []
ls = create_list(ls)
even_odd_lists(ls)