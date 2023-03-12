import math
a=float(input("Enter The Length Of First Side Of Triangle\n"))
b=float(input("Enter The Length Of Second Side Of Triangle\n"))
c=float(input("Enter The Length Of Third Side Of Triangle\n"))

s=(a+b+c)/2

area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The Area Of A Triangle Having Side Dimensions",a,b,"And",c,"Is",area,"Units")