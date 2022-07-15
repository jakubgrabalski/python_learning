class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power
    def attack(self):
        print(f'{self.name} is attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'{self.name} is attacking with number of {self.num_arrows} arrows')


wizard = Wizard('Merlin', 50, 'wizard@domain.com')
archer = Archer('Robin', 100, 'archer@domain.com')

for char in [wizard, archer]:
    char.attack()

print(wizard.email)
print(archer.email)

print(dir(wizard))
