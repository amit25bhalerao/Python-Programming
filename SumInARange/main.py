# Program To Find Sum Of A Given Range

def sum_range(ll,ul):
    total = 0
    for i in range(ll, ul+1):
        total += i
    print("The Sum Of Numbers In The Range {} And {} Is {}".format(ll,ul,total))

ll = int(input("Enter The Lower Limit: "))
ul = int(input("Enter The Upper Limit: "))
sum_range(ll,ul)
    