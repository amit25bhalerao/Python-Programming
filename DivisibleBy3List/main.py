# Even_Odd List Program
def create_list(ls):

    print("Enter 20 Values Into The List")
    while True:
        x = int(input())

        if len(ls) == 19:
            break

        ls.append(x)

    return ls

def mod_three_lists(ls):
    ls_mod3 =[]

    for i in ls:
        if i % 3 == 0:
            ls_mod3.append(i)

    print("Divisible By Three List: ", ls_mod3)

ls = []
ls = create_list(ls)
mod_three_lists(ls)