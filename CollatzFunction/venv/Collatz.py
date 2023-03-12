# Collatz Function
def collatz(number):
    if number % 2 == 0:
        x = number//2
        return x
    elif number % 2 == 1:
        y = 3 * number + 1
        return y

# Accept Number From The User
num = int(input("Enter Number: "))

while num != 1:
    num = collatz(num)
    print(num)

