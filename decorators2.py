def my_decorator(func):
    def wrap_funct():
        print('***')
        func()
        print('***')
    return wrap_funct

def other_decorator(func):
    def wrap_funct(*args, **kwargs):
        print('***')
        func(*args, **kwargs)
        print('***')
    return wrap_funct

@my_decorator
def hello():
    print('hello')

@my_decorator
def bye():
    print('bye')

hello()
bye()

@other_decorator
def other_hello(greetings, emoji):
    print(greetings, emoji)

other_hello('hello',':)')
