class PlayerCharacter:
    membership = True #Class Object Attribute
    def __init__(self, name, age):
        if self.membership:
            self.name = name #Attribute
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')
    
    def speak(self, greet):
        print(f'{greet}, my name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('John', 44)
player2 = PlayerCharacter('Tom', 22)

player1.speak('Hello') #abstract implementation, not visible to user

