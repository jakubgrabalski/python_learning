username = input('Username: \n')
password = input('Password: \n')
password_lenght = len(password)
hash = password_lenght * '*'
print(f'Hi {username}, your password {hash} is {password_lenght} chars long')

print(f'Hi {username}, your password {hash} is {len(password)} chars long')