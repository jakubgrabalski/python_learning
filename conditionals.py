age = int(input('Your age?\n'))
license = input('Do you have driver\'s license? (y/n)\n')

if age >= 0 and (license=='n' or license=='y'):
    if age >= 18 and license == 'y':
        print('You\'ve got the license and age to drive')
    elif age >=18 and license == 'n':
        print('You\'re adult enough but get the license to drive legally')
    elif age <18 and license == 'y':
        print('Your license is fake')
    else:
        print('You are too young for driver\'s licence')
else:
    print('Wrong data provided')