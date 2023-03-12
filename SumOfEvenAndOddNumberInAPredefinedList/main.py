# Assuming Predefined List To Be Set Of Integers From 1 to 10

ls = [1,2,3,4,5,6,7,8,9,10]
odd_sum = 0
even_sum = 0

for x in ls:
    if x % 2 != 0:
        odd_sum += x
    else:
        even_sum += x

print("Even Number Summation Equals ", even_sum)
print("Odd Numbers Summation Equals ", odd_sum)
