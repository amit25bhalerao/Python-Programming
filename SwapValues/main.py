# Program To Swap Two Variables Without Using Third Variable

def swap(a, b):
    print("Before Swapping A: ", a)
    print("Before Swapping B: ", b)

    a = a + b
    b = a - b
    a = a - b

    print("After Swapping A: ", a)
    print("After Swapping B: ", b)


a = int(input("Enter The First Number: "))
b = int(input("Enter The Second Number: "))

swap(a,b)