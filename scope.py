from threading import local
from xml.dom.xmlbuilder import DOMEntityResolver


def some_func():
    total = '100'
    print(total)

some_func()

x='hello'[0]
print(x)


a = 1
def parent():
#    a = 10
    def confusion():
        return a
    return confusion()

print(parent())
    
#variables priority:
#1 - local
#2 - parent 
#3 - global 
#4 - python predefined

