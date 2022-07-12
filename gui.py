picture = [ 
    [0,0,0,1,0,0,0], 
    [0,0,1,1,1,0,0], 
    [0,1,1,1,1,1,0], 
    [1,1,1,1,1,1,1], 
    [0,0,0,1,0,0,0], 
    [0,0,0,1,0,0,0] 
]

for row in picture:
    for pixel in row:
        if (pixel == 0):
             print(' ', end='')
        else: print('*', end='')
    print('')

####### 
# Cleaner code

picture = [ 
    [0,0,0,1,0,0,0], 
    [0,0,1,1,1,0,0], 
    [0,1,1,1,1,1,0], 
    [1,1,1,1,1,1,1], 
    [0,0,0,1,0,0,0], 
    [0,0,0,1,0,0,0] 
]

fill = '*'
empty = ' '

for row in picture:
    for pixel in row:
        if pixel:
             print(fill, end='')
        else: print(empty, end='')
    print('')    