# Program To Check Voters Eligibility

def voter(age):
    if age >= 18:
        return 'Eligible'
    else:
        return 'Not Eligible'

age = int (input('Enter The Age Of The Person: '))
print('The Person Is {} For Voting'.format(voter(age)))