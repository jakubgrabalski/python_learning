from operator import ne


my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

user = {
    (1,2) : [1,2,3], #tuple as index
    'greet' : 'hello'
}
print(user[(1,2)])

new_tuple = my_tuple[1:3]
print(new_tuple)

x,y,z, *other = (1,2,3,4,5)

print(x)
print(other)
print(my_tuple.index(5))
print(len(my_tuple))