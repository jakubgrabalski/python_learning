def say_simple_hello():
    print('hello')

say_simple_hello()

def say_hello(name='John', emoji=']:->'):
    print(f'hello {name} {emoji}')

say_hello('John',':)')


# keyword arguments
say_hello(emoji=':P', name='Bibi') #baaaad 
say_hello(name='Bibi', emoji=':P') #good 
say_hello()
say_hello('Timmy')