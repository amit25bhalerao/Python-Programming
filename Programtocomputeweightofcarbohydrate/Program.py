def main():
    h = int(input("Enter The Number Of Hydrogen Atoms\n"))
    o = int(input("Enter The Number Of Oxygen Atoms\n"))
    c = int(input("Enter The Number Of Carbon Atoms\n"))

    w = h * 1.00794 + o * 15.9994 + c * 12.0107

    print("The Weight Of Carbohydrate Is", w)

main()
