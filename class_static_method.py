class PlayerCharacter:
    membership = True #Class Object Attribute
    def __init__(self, name, age):
        self.name = name #Attribute
        self.age = age

    def shout(self):
        print(f'My name is {self.name}')
    
    @classmethod
    def adding_thigs(cls, num1, num2):
        return cls('Ted', num1 + num2)

    @staticmethod
    def adding_thigs2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('John', 44)
player2 = PlayerCharacter('Tom', 22)
player3 = PlayerCharacter.adding_thigs(2,3)
player4 = PlayerCharacter.adding_thigs2(5,3)

print(player1.membership)
print(player1.name)


player2.shout() 

print(player3.age)
