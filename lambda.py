# lambda param: action(param)

from functools import reduce


my_list = [1,2,3]
a = [(0,2), (4,3), (10, -1)]

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item%  2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))


print(list(map(lambda item: item**2, my_list)))
a.sort(key=lambda x: x[1])
print(a)