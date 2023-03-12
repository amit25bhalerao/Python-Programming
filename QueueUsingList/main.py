def queue_list(queue):
    while True:
        print("Enter 1: Add Element To The Queue")
        print("Enter 2: Remove Element From The Queue")
        print("Enter 3: Print The Queue")
        print("Enter 4: Exit")
        x = int(input("Enter Your Choice: "))

        if x == 1:
            val = int(input("Enter The Element To Be Added Into The Queue: "))
            queue.append(val)
            print(val, " Inserted Successfully")

        elif x == 2:
            if len(queue) == 0:
                print("Queue Is Empty. Nothing To Be Removed")
            else:
                print(queue.pop(0), " Removed Successfully")

        elif x == 3:
            if len(queue) == 0:
                print("Queue Is Empty")
            else:
                print("Queue: ", queue)

        else:
            print('Thank You')
            exit()

queue=[]
queue_list(queue)