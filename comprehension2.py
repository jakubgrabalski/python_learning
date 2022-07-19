from lib2to3.pgen2.literals import simple_escapes


my_set1 = {char for char in 'hello'}
my_set2 = {number for number in range(0,100)}
my_set3 = {number*2 for number in range(0,100)}
my_set3 = {number**2 for number in range(0,100) if (number % 2 == 0)}


print(my_set1)
print(my_set2)
print(my_set3) 



simple_dict = {
    'a' : 1,
    'b' : 2
    }

dict = {k:v**2 for k, v in simple_dict.items()}

print(dict) 


dict = {num:num*2 for num in [1,2,3]}

print(dict) 

alist = ['a','b','c','c','a']
dict = list(set([num for num in alist if alist.count(num) > 1]))
print(dict) 
