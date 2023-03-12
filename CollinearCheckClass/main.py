class CollinearCheck:
    """Attributes: X1, Y1, X2, Y2, X3, Y3"""

    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def collinear(self):
        Area = 0.5 * (self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2))
        if Area == 0.0:
            print("The Given Points Are Collinear In Nature")
        else:
            print("The Given Points Aren't Collinear In Nature")


X1 = float(input("Enter Value Of X1: "))
Y1 = float(input("Enter Value Of Y1: "))
X2 = float(input("Enter Value Of X2: "))
Y2 = float(input("Enter Value Of Y2: "))
X3 = float(input("Enter Value Of X3: "))
Y3 = float(input("Enter Value Of Y3: "))
c = CollinearCheck(X1, X2, X3, Y1, Y2, Y3)
c.collinear()
