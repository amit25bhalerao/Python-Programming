import copy
import math


class Point:
    """Represents a Point.
    Attributes: x, y
    """


class Rectangle:
    """ Represents a rectangle
    attributes:width,height,corner
    """


def distance_between_points(p1,p2):
    return math.sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))


class Circle:
    """Represents a circle.
    Attributes: center, radius
    """


def print_point(p):
    print('(%g,%g)'%(p.x, p.y))


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).
    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    print("Distance Between Centre Of Circle And Given Point Co-Ordinates Is:  ", d)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)

    if not point_in_circle(p, circle):
        return False
    p.x += rect.width

    if not point_in_circle(p, circle):
        return False
    p.y -= rect.height

    if not point_in_circle(p, circle):
        return False
    p.x -= rect.width

    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)

    if point_in_circle(p, circle):
        return True
    p.x += rect.width

    if point_in_circle(p, circle):
        return True
    p.y -= rect.height

    if point_in_circle(p, circle):
        return True
    p.x -= rect.width

    if point_in_circle(p, circle):
        return True

    return False


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 50.0
box.corner.y = 50.0
print("X Co-Ordinate Of Corner Of Box: ", box.corner.x)
print("Y Co-Ordinate Of Corner Of Box: ", box.corner.y)


circle = Circle
circle.center = Point()
circle.center.x = 150.0
circle.center.y = 100.0
circle.radius = 75.0

print("X Co-Ordinate Of Centre Of Circle: ", circle.center.x)
print("Y Co-Ordinate Of Centre Of Circle: ", circle.center.y)
print("Radius Of The Circle: ", circle.radius)


print("***************************************************************************************************************")
print("Is Point Present Within The Circle?", point_in_circle(box.corner, circle))
print("***************************************************************************************************************")
print("Is Rectangle Present Within The Circle?", rect_in_circle(box, circle))
print("***************************************************************************************************************")
print("Does The Rectangle And Circle Overlap?", rect_circle_overlap(box, circle))
print("***************************************************************************************************************")