from tokenize import Triple


class PlayerCharacter:
    membership = True #Class Object Attribute
    def __init__(self, name, age):
        if self.membership:
            self.name = name #Attribute
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')
    
    def run(self, hello):
        print(f'{hello} my name is {self.name}')


player1 = PlayerCharacter('John', 44)
player2 = PlayerCharacter('Tom', 22)
player2.attack = 50

print(player1.membership)
print(player2.membership)
print(player1.name)
print(player2.shout())
print(player2.run('Hi'))