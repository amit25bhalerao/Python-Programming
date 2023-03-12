class Complex():

    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: "))

    def display(self):
        print(self.realPart,"+",self.imgPart,"i", sep="")

    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart

    def diff(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart

    def mul(self, c1, c2):
        self.realPart = c1.realPart * c2.realPart
        self.imgPart = c1.imgPart * c2.imgPart


c1 = Complex()
c2 = Complex()
c3 = Complex()
c4 = Complex()
c5 = Complex()

print("Enter First Complex Number")
c1.initComplex()
print("First Complex Number: ", end="")
c1.display()

print("Enter Second Complex Number")
c2.initComplex()
print("Second Complex Number: ", end="")
c2.display()

print("Sum Of Two Complex Numbers Is: ", end="")
c3.sum(c1, c2)
c3.display()

print("Difference Of Two Complex Numbers Is: ", end="")
c4.diff(c1, c2)
c4.display()

print("Multiplication Of Two Complex Numbers Is: ", end="")
c5.mul(c1, c2)
c5.display()
