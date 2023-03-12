# Program To Check The Quadrant In Which The Co-Ordinate Lies

def coordinate(x,y):
    if x >= 0 and y >= 0:
        print("({},{}) Lies In First Quadrant".format(x,y))
    elif x <= 0 and y >= 0:
        print("({},{}) Lies In Second Quadrant".format(x, y))
    elif x <= 0 and y <= 0:
        print("({},{}) Lies In Third Quadrant".format(x, y))
    else:
        print("({},{}) Lies In Fourth Quadrant".format(x, y))


x_pos = int (input("Enter The X Co-Ordinate (0-90): "))
y_pos = int (input("Enter The Y Co-Ordinate (0-90): "))

coordinate(x_pos,y_pos)