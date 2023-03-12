# Program For Countdown To Zero

def countdown(num):
    print("The Countdown Begins From {} To O".format(num))
    while num >= 0:
        print(num)
        num -= 1

num = int(input("Enter The Value Of N: "))
countdown(num)