# Python Program to find Area Of Circle using Radius

def circle():
    PI = 3.14
    radius = float(input("Enter The Radius Of The Circle: "))
    area = PI * radius * radius
    circumference = 2 * PI * radius

    print(" Area Of a Circle = ",area, "Units")
    print(" Circumference Of a Circle = ", circumference, "Units")

circle()