def armstrong(n):
    temp=n
    sum=0
    while(n!=0):
        digit=n%10
        sum=sum+digit*digit*digit
        n=n//10
    if(sum==temp):
        return 1
    else:
        return 0

n=(int(input("\nEnter A Number\n")));

res=armstrong(n)

if(res==1):
    print(n," Is An Armstrong Number\n")
else:
    print(n," Isnt An Armstrong Number\n")