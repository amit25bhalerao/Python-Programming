# Even_Odd List Program
def create_list(ls):
    total = 0
    count = 0
    while True:
        x = int(input())
        ls.append(x)
        total += x
        count += 1
        if count == 5:
            break

    print("Sum Values: ", total)

print("Enter Values Into The List")
ls = []
create_list(ls)

