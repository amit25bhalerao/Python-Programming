def harshadcheck(n):
    temp=n
    sum=0
    while(n!=0):
        digit = n % 10
        sum = sum + digit
        n = n // 10
    if(temp%sum==0):
        return 1
    else:
        return 0

n=(int(input("\nEnter A Number\n")))

res=harshadcheck(n)

if(res==1):
    print(n,"Is A Harshad Number\n")
else:
    print(n,"Isnt A Harshad Number\n")
