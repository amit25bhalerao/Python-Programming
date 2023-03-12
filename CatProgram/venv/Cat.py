# Program To Accept Multiple Cat Names And Display Them

catnames = []
count = 0

while True:
    name = input("Enter The Name Of Cat "+str(len(catnames)+1)+" Or Press Enter To Exit: ")
    if name == '':
        break
    catnames = catnames + [name]
    count = count +1

if count == 0:
    print("There Are No Cats")
else:
    print("The Cat Names Are Displayed Below")
    for name in catnames:
        print("\t"+name)