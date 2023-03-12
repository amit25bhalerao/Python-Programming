
def arcLength (diameter, angle):
    if angle >= 360:
        print("Angle Cannot Be Formed. Hence, No Value Of Arc Length Can Be Calculated.")
        exit(0)
    else:
        arc = (3.142857142857143 * diameter) * (angle / 360.0)
        return arc

diameter = float(input("Enter The Value Of Diameter: "))
angle = float(input("Enter The Value Of Angle: "))
arc_len = arcLength(diameter, angle)
print("Arc Length: {} Units".format(arc_len))
