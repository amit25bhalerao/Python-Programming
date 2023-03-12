# Program To Find The Maximum Of 3 Numbers

# Accept 3 Numbers From User
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))

# Logic To Calculate Maximum Of 3 Numbers
if num1>num2 and num1>num3:
    print("{} Is The Maximum Of {},{},{}".format(num1, num1, num2, num3))
elif num2>num1 and num2>num3:
    print("{} Is The Maximum Of {},{},{}".format(num2,num1, num2, num3))
else:
    print("{} Is The Maximum Of {},{},{}".format(num3, num1, num2, num3))