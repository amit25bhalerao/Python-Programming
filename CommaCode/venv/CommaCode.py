# Program Accepts A List, Seprate The List With Comma And Add "and" Before The Last Item In The List

def acceptlist(spamlist):
    returnstring = ''

    for i in range (len(spamlist)):
        if i == len(spamlist)-1:
            returnstring += 'and ' + spamlist[i]
        else:
            returnstring += spamlist[i] + ', '

    return returnstring

spam= ['Apples', 'Banana', 'Tofu', 'Cats']
result = acceptlist(spam)
print(result)