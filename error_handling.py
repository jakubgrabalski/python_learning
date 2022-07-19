while True:
    try:
        age = int(input('What is your age? '))
        10/age
        raise ValueError('Come on! ')
#    except ValueError: 
#        print('Please enter a number! ')
        continue
    except ZeroDivisionError: 
        print('Please enter an age higher than 0! ')    
        break
    else:
        print('Thanks!')
        break
    finally:
        print('Input provided')
 