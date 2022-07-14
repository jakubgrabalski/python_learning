class PlayerCharacter:
    membership = True #Class Object Attribute
    def __init__(self, name='anonymous', age=0):
        if (age>18):
            self.name = name #Attribute
            self.age = age

    def shout(self): 
        print(f'My name is {self.name}')
    
    def run(self, hello):
        print(f'{hello} my name is {self.name}')


player1 = PlayerCharacter('John', 19)
player2 = PlayerCharacter('Tom', 22)
player2.attack = 50

print(player1.membership)
print(player1.name)
print(player1.shout())
print(player1.run('Hi'))