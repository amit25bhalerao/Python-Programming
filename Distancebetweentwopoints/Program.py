import math

# Program To Find Distance Between Two Points

def main():

    # Accept First Point Co-Ordinates
    print("Enter The First Point Coordinates")
    x1=float(input("X1:"))
    y1=float(input("Y1:"))

    # Accept Second Point Co-Ordinates
    print("Enter The Second Point Coordinates")
    x2 = float(input("X2:"))
    y2 = float(input("Y2:"))

    # Calculate Distance Between Two Points
    distance = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

    # Display Output To The User
    print("The Distance Of Line Joining The Given Coordinates Is {} Units".format(distance))

main()