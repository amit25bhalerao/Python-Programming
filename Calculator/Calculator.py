def calculator():
    print("Welcome!")
    print("Enter 1: Addition")
    print("Enter 2: Subtraction")
    print("Enter 3: Multiplication")
    print("Enter 4: Division")
    print("Enter 5: Quit")
    choice = int(input("Enter Your Choice: "))
    if 0 < choice < 6:
        if choice == 1:
            n1 = float(input("Enter First Operand: "))
            n2 = float(input("Enter Second Operand: "))
            res = n1 + n2
            print(n1, "+", n2, "=", res)
        elif choice == 2:
            n1 = float(input("Enter First Operand: "))
            n2 = float(input("Enter Second Operand: "))
            res = n1 - n2
            print(n1, "-", n2, "=", res)
        elif choice == 3:
            n1 = float(input("Enter First Operand: "))
            n2 = float(input("Enter Second Operand: "))
            res = n1 * n2
            print(n1, "*", n2, "=", res)
        elif choice == 4:
            n1 = float(input("Enter First Operand: "))
            n2 = float(input("Enter Second Operand: "))
            try:
                res = n1 / n2
                print(n1, "-", n2, "=", res)
            except:
                print("Syntax Error")
        else:
            print("Thank You! The Program Will Quit")
            exit(0);
    else:
        print("Invalid Input Entered.. Please Try Again")

while True:
    calculator()