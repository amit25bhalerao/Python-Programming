from collections import Counter
my_dict = {'Item1': 45.50, 'Item2': 25, 'Item3': 41.3, 'Item4': 55, 'Item5': 24}

k = Counter(my_dict)

# Finding 3 highest values
high = k.most_common(3)

print("The Top 3 Items In The Shop Are: ")
print("Keys: Values")

for i in high:
   print(i[0]," :",i[1]," ")