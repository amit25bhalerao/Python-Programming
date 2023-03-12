import math

def main():
    r=float(input("Enter The Radius Of The Pizza In Centimeters\n"))
    r=r/0.393701
    a=math.pi*r*r
    p=float(input("Enter The Price Of The Pizza\n"))
    print("The Cost Per Square Inch Of The Circular Pizza Of Area",a,"Units Is ",p/r)

main()