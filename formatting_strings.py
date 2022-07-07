name = 'John'
age = 45
print('Hi ' + name + ' You are ' + str(age) + ' years old')

print(f'Hi {name} You are {age} years old')

print('Hi {} You are {} years old'.format('Noe','33'))

print('Hi {} You are {} years old'.format(name,age))

print('Hi {1} You are {0} years old'.format(name,age))
# overwritting
print('Hi {new_name} You are {new_age} years old'.format(new_name = 'Elon',new_age = 35))
