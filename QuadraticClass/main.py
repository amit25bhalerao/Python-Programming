import cmath


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    def roots(self):
            x = (-self.b + cmath.sqrt(self.discriminant())) / (2 * self.a)
            y = (-self.b - cmath.sqrt(self.discriminant())) / (2 * self.a)
            print("First Root: ", x)
            print("Second Root: ", y)


a = int(input("Enter The Value Of A: "))
b = int(input("Enter The Value Of B: "))
c = int(input("Enter The Value Of C: "))
q = QuadraticEquation(a, b, c)
q.roots()