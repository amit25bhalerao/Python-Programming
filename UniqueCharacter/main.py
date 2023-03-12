ls = {}
string = input("Enter Your String: ")
res = []

for c in string:
    if c not in ls:
      res.append(c)
      ls[c]=1

print("The Resultant String Is: ",end=" ")
print("".join(res))