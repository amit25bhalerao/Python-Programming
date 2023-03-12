class QuadrantCheck:
    """Attributes: X Co-Ordinate And Y Co-Ordinate"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinate(self, x, y):
        if x > 0 and y > 0:
            print("({},{}) Lies In First Quadrant".format(x, y))
        elif x < 0 and y > 0:
            print("({},{}) Lies In Second Quadrant".format(x, y))
        elif x < 0 and y < 0:
            print("({},{}) Lies In Third Quadrant".format(x, y))
        elif x > 0 and y < 0:
            print("({},{}) Lies In Fourth Quadrant".format(x, y))
        elif x == 0 and y > 0:
            print("({},{}) Lies At Positive Y - Axis".format(x, y))
        elif x == 0 and y < 0:
            print("({},{}) Lies At Negative Y - Axis".format(x, y))
        elif y == 0 and x < 0:
            print("({},{}) Lies At Negative X - Axis".format(x, y))
        elif y == 0 and x > 0:
            print("({},{}) Lies At Positive X - Axis".format(x, y))
        else:
            print("({},{}) Lies At Origin".format(x, y))


x_pos = int(input("Enter The X Co-Ordinate (0-90): "))
y_pos = int(input("Enter The Y Co-Ordinate (0-90): "))

Check = QuadrantCheck(x_pos, y_pos)
Check.coordinate(x_pos, y_pos)
