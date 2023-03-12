from turtle import*
import time

def main():
    while 1:
        n=(input("Enter 'Yes' To Draw Polygon Or 'No' To Exit\n"))

        if(n=='Yes'):
            amit = Turtle()
            side = int(input("Enter The Number Of Sides In Polygon\n"))
            length = float(input("Enter The Length Of The Side Of Polygon\n"))
            extangle = 360 // side

            for i in range(1, side + 1):
                amit.forward(length)
                amit.left(extangle)

            time.sleep(10)
            amit.clear()

        else:
            print("Thank You :) :)")
            exit(0)

main()