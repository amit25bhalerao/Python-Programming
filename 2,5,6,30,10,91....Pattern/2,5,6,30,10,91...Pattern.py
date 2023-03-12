def main():
    n=eval(input("Enter The Value Of N\n"))
    sum=temp=0

    for i in range(1,n+1):
        if(i%2!=0):
            temp=2*i
            print(temp,end=" ")
        sum=sum+i*i
        if((i%2)==0):
            print(sum,end=" ")

main()