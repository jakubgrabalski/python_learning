class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('John', 44)
player2 = PlayerCharacter('Tom', 22)
player2.attack = 50

print(f'{player1.name}, {player1.age}')
print(player2.name)
print(player2.run())
print(player2.attack)
