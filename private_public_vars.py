class PlayerCharacter:
    def __init__(self, name, age):
        if self.membership:
            self._name = name #no true private var in python. agreed to do not touch variables with _ in name
            self._age = age

    def shout(self):
        print(f'My name is {self.name}')
    
    def speak(self, greet):
        print(f'{greet}, my name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('John', 44)
player2 = PlayerCharacter('Tom', 22)

player1.speak('Hello') 