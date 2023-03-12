def palindrome(num):
    temp = num
    sum=0

    while(num!=0):
        digit=num%10
        sum=(sum*10)+digit
        num=num//10

    if(temp==sum):
        return 1
    else:
        return 0



a=(int(input("\nEnter A Number\n")))

res=palindrome(a)

if(res==1):
    print(a,"Is A Palindrome Number")
else:
    print(a,"Isnt A Palindrome Number")