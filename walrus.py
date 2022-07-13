# :=

a = 'helloooooo'
if (len(a) > 5):
    print(f'foo long {len(a)} is more than 5 elements')

if ((n := len(a)) > 5):
    print(f'foo long {n} is more than 5 elements')

while ((n := len(a)) > 5):
    print(f'word: {a}, has: {n} elements')
    a = a[:-1]