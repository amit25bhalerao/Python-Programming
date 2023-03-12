x = int(input("Enter A Number: "))
print("Left Aligned (Width 10): "+" {:< 10d}".format(x))
print("Right Aligned (Width 10): "+" {:10d}".format(x))
print("Center Aligned (Width 10): "+" {:^10d}".format(x))