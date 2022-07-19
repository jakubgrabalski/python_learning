my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)


my_list1 = [char for char in 'hello']
my_list2 = [number for number in range(0,100)]
my_list3 = [number*2 for number in range(0,100)]
my_list3 = [number**2 for number in range(0,100) if (number % 2 == 0)]


print(my_list1)
print(my_list2)
print(my_list3)