my_list = [1,2,3,4,5,5,4,3,2,1]
my_set = {1,2,3,4,5,5,4,3,2,1}

my_set.add(100)
my_set.add(1)
print(my_set)
print(my_list)

set_array = set(my_list)
print(set_array)

print(set(my_list))

#python3 set.py - set shows only unique values
#{1, 2, 3, 4, 5, 100}

# print (my_set[0]) - do not work
print(1 in my_set)

my_set1 = my_set.copy()
print(list(my_set1)) 