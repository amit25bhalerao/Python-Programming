# Program To Check Whether A Year Is A Leap Year Or Not

def leapyear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 4 ==0))

year = int (input("Enter A Year: "))
if leapyear(year):
    print('{} Is A Leap Year'.format(year))
else:
    print('{} Is Not A Leap Year'.format(year))


