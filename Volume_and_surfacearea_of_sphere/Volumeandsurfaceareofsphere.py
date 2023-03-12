import math
def main():
    r=float(input("Enter The Radius Of The Sphere\n"))
    v=(4.0/3)*math.pi*r*r*r
    a=4*math.pi*r*r
    print("The Surface Area Of The Given Sphere Is",a," Units")
    print("The Volume Of The Given Sphere Is",v," Units")

main()