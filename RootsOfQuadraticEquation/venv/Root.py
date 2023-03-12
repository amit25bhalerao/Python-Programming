# Program To Find Roots Of A Quadratic Equation

import cmath

print ("The Quadratic Equation Is Of The Form: Ax^2 + Bx + C, Where A, B And C Are Constants.")
a = int (input("Enter The Value Of A: "))
b = int (input("Enter The Value Of B: "))
c = int (input("Enter The Value Of C: "))

temp = cmath.sqrt((b*b)-(4*a*c))

x = (-b + temp) / ( 2 * a )
y = (-b - temp) / ( 2 * a )

print('X = {} \nY = {}'.format(x,y))