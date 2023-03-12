class Point(object):
    "Represents A Point In 2-D Space"

class Rectangle(object):
    """Represents A Rectangle.
    Attributes: Width, Height, Corner"""

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


box = Rectangle()
box.width = input("Enter The Width Of The Rectangle: ")
box.height = input("Enter The Height Of The Rectangle: ")
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print("Dimensions Of Rectangle - Width = {} Units".format(box.width))
print("Dimensions Of Rectangle - Height = {} Units".format(box.height))
print("Initial Value Of X Co-Ordinate Representing Bottom Left Corner Of The Rectangle: ", box.corner.x)
print("Initial Value Of Y Co-Ordinate Representing Bottom Left Corner Of The Rectangle: ", box.corner.y)


dx = float(input("Enter The Value Of dx By Which You Wish To Move The Position Of Rectangle: "))
dy = float(input("Enter The Value Of dy By Which You Wish To Move The Position Of Rectangle: "))


move_rectangle(box, dx, dy)


print("Updated Value Of X Co-Ordinate Representing Bottom Left Corner Of The Rectangle: ", box.corner.x)
print("Updated Value Of Y Co-Ordinate Representing Bottom Left Corner Of The Rectangle: ", box.corner.y)

