# Program To Check Whether A Number Is Positive, Negative Or Zero.

def numbercheck(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

number = int (input ("Enter A Number: "))
print('Number Is {}'.format(numbercheck(number)))