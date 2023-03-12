n=(int(input("\nEnter The Value of N\n")))

for i in range (1,n+1):
    for j in range (1,i+1):
        if(j==i):
            for k in range(1,i+1):
                print(i," ",end="")
    print("")