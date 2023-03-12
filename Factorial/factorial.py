def fact(n):
    if(n==0):
        return 1
    return fact(n-1)*n

a=int(input("Enter The Number Whose Factorial Is To Be Found Out\n"))

res=fact(a)

print("The Factorial Of ",a," Is ",res)