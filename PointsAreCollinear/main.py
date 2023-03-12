X1 = float(input("Enter Value Of X1: "))
Y1 = float(input("Enter Value Of Y1: "))
X2 = float(input("Enter Value Of X2: "))
Y2 = float(input("Enter Value Of Y2: "))
X3 = float(input("Enter Value Of X3: "))
Y3 = float(input("Enter Value Of Y3: "))

Area = 0.5 * (X1 * (Y2 - Y3) + X2 * (Y3 - Y1) + X3 * (Y1 - Y2))

if Area == 0.0:
    print("The Given Points Are Collinear In Nature")
else:
    print("The Given Points Aren't Collinear In Nature")