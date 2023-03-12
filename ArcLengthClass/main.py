class ArcLength:
    """Attributes: Diameter, Angle"""

    def __init__(self, diameter, angle):
        self.diameter = diameter
        self.angle = angle

    def arcLength(self):
        if self.angle >= 360:
            print("Angle Cannot Be Formed. Hence, No Value Of Arc Length Can Be Calculated.")
            exit(0)
        else:
            arc = (3.142857142857143 * self.diameter) * (self.angle / 360.0)
            return arc


dia = float(input("Enter The Value Of Diameter: "))
agl = float(input("Enter The Value Of Angle: "))

a = ArcLength(dia, agl)

arc_len = a.arcLength()
print("Arc Length: {} Units".format(arc_len))
