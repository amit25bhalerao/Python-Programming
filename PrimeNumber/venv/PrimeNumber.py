
def prime(n):
    if(n>1):
        for i in range(2, n):
            if (n % i == 0):
                print(n,"Isnt Prime Number")
                break
            else:
                print(n,"Is A Prime Number")
                break
    else:
        print(n,"Isnt A Prime Number")


a=(int(input("\nEnter A Number\n")))

prime(a)
