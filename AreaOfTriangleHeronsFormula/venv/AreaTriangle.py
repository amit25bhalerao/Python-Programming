#Program To Calculate Area Of Triangle Using Herons Formula

import math

# Accept Length Of 3 Sides Of The Triangle
a=int(input("Enter The Length Of First Side: "))
b=int(input("Enter The Length Of Second Side: "))
c=int(input("Enter The Length Of Third Side: "))

s=(a+b+c)/2

# Logic To Calculate Area Of Triangle
areatriangle = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The Area Of Triangle Using Herons Formula Is {} Units".format(areatriangle))
