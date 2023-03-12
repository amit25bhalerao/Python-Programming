dict = {'Tom': [70, 80, 86, 44], 'Harry': [65, 77, 45, 88], 'Alice': [88,99,76,89], 'Kevin': [99, 66, 76, 81]}
print("Original Dictionary: ", dict)

sum_dict = {k: sum(v) for k, v in dict.items()}
print("Dictionary Having Values Representing Sum Of Scores Secured By A Student: ",sum_dict)

print("Topper Score Is: ", max(sum_dict.values()))

v = list(sum_dict.values())
k = list(sum_dict.keys())
topper_index = k[v.index(max(v))]

print("Topper Name: ", topper_index)