class Wizard():
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def magic(self):
        print(f'{self.name} is attacking with power of {self.power}')

class Archer():
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name} is attacking with number of {self.num_arrows} arrows')

    def run(self):
        print((f'{self.name} is running away'))

class MagicArcher(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer().__init__(self, name, num_arrows)
        Wizard().__init__(self, name, power)


wizard = Wizard('Merlin', 50)
archer = Archer('Robin', 100)
magicarcher = MagicArcher('Legolas', 50, 60)


print(wizard.magic())
print(magicarcher.attack())