def main():
    print("Enter The First Point Coordinates")
    x1=float(input("X1:"))
    y1=float(input("Y1:"))
    print("Enter The Second Point Coordinates")
    x2 = float(input("X2:"))
    y2 = float(input("Y2:"))

    slope=(y2-y1)/(x2-x1)

    print("The Slope Of Line Joining The Given Coordinates Is ",slope)

main()