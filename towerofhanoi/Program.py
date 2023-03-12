def tower(n,source,temp,destination):
    if(n==0):
        return
    tower(n-1,source,destination,temp)
    print("Move",n,"From Peg",source,"To Peg",destination)
    tower(n-1,temp,source,destination)



def main():
    n = int(input("Enter The Total Number Of Disks\n"))
    source = 'A'
    temp = 'B'
    destination = 'C'


    tower(n,source,temp,destination)

main()
