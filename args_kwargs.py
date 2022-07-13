def super_func(*args):
    return sum(args)

print(super_func(1,2,3))


def super_func2(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) +  total

print(super_func2(1,2,3, num1=1, num2=10))


