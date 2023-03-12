# Program To Find Area Of A Circle

import math

# Accepting Radius From The User
radius = float(input("Enter The Radius Of The Circle: "))

# Calculate Area Of Circle
areacircle = math.pi * radius * radius

# Display Output To The User
print("The Area Of Circle With Radius {} Is {} Units".format(radius, areacircle))
