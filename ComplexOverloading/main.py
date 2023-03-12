class Complex:
    # Defining init Method For Class
    def __init__(self, r, i):
        self.real = r
        self.img = i

    # Overloading The Add Operator Using Special Function
    def __add__(self, other):
        r = self.real + other.real
        i = self.img + other.img
        return complex(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.img - other.img
        return complex(r, i)

    # string function to print object of Complex class
    def __str__(self):
        return str(self.real)+' + '+str(self.img)+'i'


c1 = Complex(5, 5)
c2 = Complex(2, 4)
print("Sum Of Two Complex Numbers: ", c1 + c2)
print("Difference Of Two Complex Numbers: ", c1 - c2)