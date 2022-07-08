from datetime import date

name = 'Andy Doe'
age = 50
relationship_status = 'single'

relationship_status = 'it\'s complicated'
print(relationship_status)

birth_year = input('What year were you born\n')
year = date.today().year
age = year - int(birth_year)

print('Your age is', year - int(birth_year))
# or
print(f'Your age is {age}')
