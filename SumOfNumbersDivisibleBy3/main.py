# Even_Odd List Program
def create_list(ls,n):
    total = 0
    while True:
        x = int(input())
        ls.append(x)
        if len(ls) == n:
            break

    for i in ls:
        if i % 3 == 0:
            total += i

    print("Sum Of All Numbers Divisible By 3 In The Given List Is: ", total)

n = int(input("Enter The Value Of N: "))
ls = []
create_list(ls,n)

