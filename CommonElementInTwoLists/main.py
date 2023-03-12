# Program To Find If There Exists A Common Element In Both The Lists
def create_list(ls):
    # Press Anything Other Than Enter To Stop Accepting The Input
    while True:
        x = input()

        if x == "":
            break

        ls.append(x)

    return ls


ls1 = []
ls2 = []

print("Enter Elements Into List 1")
ls1 = create_list(ls1)
print("List 1 Elements: ", ls1)

print("Enter Elements Into List 2")
ls2 = create_list(ls2)
print("List 2 Elements: ", ls2)

for i in ls1:
    for j in ls2:
        if i == j:
            print("Result: True, Atleast One Common Element Found")
            exit()

print("Result: False, No Common Element Found")