age = int(input('Your age?\n'))
license = input('Do you have driver\'s license? (Y/N)\n')

if age >= 18 and license == 'Y':
    print('You\'ve got the license and age to drive')
elif age >=18 and license == 'N':
    print('You\'re adult enough but get the license to drive legally')
elif age <18 and license == 'Y':
    print('Your license is fake')
else:
    print('You are too young for driver\'s licence or provided wrong answers. Try again')
