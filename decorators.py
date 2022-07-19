def hello(func):
    func()

def greet():
    print('hello')

#greet = hello
#del hello
#hello() - deleting hello will not delete greet functionality
#greet()

a = hello(greet)

print(a)
a

def greetz(func):
    func()

def greet2():
    def func():
        return 5
    return func
