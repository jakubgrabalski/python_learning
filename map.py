from functools import reduce


my_list = [1,2,3]
your_list = [10,20,30]

def multipy_by2(item):
    return item*2

def check_odd(item):
    return item %2 != 0

def accumulate(acc, item):
    print(acc, item)
    return acc + item

print(list(map(multipy_by2, my_list)))
print(list(filter(check_odd, my_list)))
print(list(zip(my_list, your_list)))

print(reduce(accumulate, my_list, 0))

print(my_list)