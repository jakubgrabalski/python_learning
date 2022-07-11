user = {
    'basket' : [1,2,3],
    'greet' : 'hello'
}

user2 = dict(name = 'John') #other way how to create dictionary


print(user.get('age', 55)) # define default value
print(user2)
print('basket' in user) #bool value if exist

print(user.items())
user2 = user.copy()


user.clear()
user2.pop('greet')
print(user.items())
print(user2.items())
user2.update({'greet': 'Hi'})
print(user2.items())
