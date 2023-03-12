def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)



n=(int(input("Enter The Value Of N To Find Out Nth Fibonacci Number\n")))


for i in range(1,n+1):
    res1=fibonacci(i)
    print(res1, end=" ")

print()

print("In The Above Fibonacci Series, The",n,"th Fibonacci Number Is",res1)

