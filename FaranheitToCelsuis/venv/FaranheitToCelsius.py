# Program To Convert Faranheit To Celsuis

#Accept Faranheit Temperature From User
fhnt = float(input("Enter The Temperature In Faranheit: "))

# Convert To Celsius
clus = ((fhnt-32)*5)/9

print("{} Units In Farenhite Equals {:.15f} Celsius Units".format(fhnt,clus))
