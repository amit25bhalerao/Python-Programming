class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width

    def __gt__(self, other):
        if self.rectangle_area() > other.rectangle_area():
            return True
        else:
            return False


Rectangle1 = Rectangle(71, 12)
print("The Area Of Rectangle 1: ", Rectangle1.rectangle_area(), "Units")

Rectangle2 = Rectangle(15, 17)
print("The Area Of Rectangle 2: ", Rectangle2.rectangle_area(), "Units")

if Rectangle1 > Rectangle2:
    print("Area Of Rectangle1 Is Greater Than Rectangle2")
else:
    print("Area Of Rectangle2 Is Greater Than Rectangle1")