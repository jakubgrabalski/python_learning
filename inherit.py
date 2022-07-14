class User:
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'Attacking with number of {self.num_arrows} arrows')


wizard = Wizard('Merlin', 50)
archer = Archer('Robin', 100)

wizard.attack()
archer.attack()
