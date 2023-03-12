def stack_list(stack):

    while True:
        print("Enter 1: Add Element To The Stack")
        print("Enter 2: Remove Element From The Stack")
        print("Enter 3: Print The Stack")
        print("Enter 4: Exit")
        x = int(input("Enter Your Choice: "))

        if x == 1:
            val = int(input("Enter The Element To Be Added Into The Stack: "))
            stack.append(val)
            print(val, " Inserted Successfully")

        elif x == 2:
            if len(stack) == 0:
                print("Stack Is Empty. Nothing To Be Removed")
            else:
                print(stack.pop(), " Removed Successfully")

        elif x == 3:
            if len(stack) == 0:
                print("Stack Is Empty")
            else:
                print("Stack: ", stack)

        else:
            print('Thank You')
            exit()

stack = []
stack_list(stack)