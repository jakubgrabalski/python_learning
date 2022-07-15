class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {'name':'yoyo', 'has_pets': False}

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'Yess??'

    def __getitem__(self, i):
        return self.my_dict[i]

    def __reduce_ex__(self):
        return 'I am reduced!!'

    def __format__(self):
        return 'I am formatted!!'

    def __repr__(self):
        return f'{self.color}'

action_figure = Toy('red',0)


print(action_figure)
print(action_figure.__str__())
print(action_figure())
print(action_figure['name'])

