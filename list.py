# li = ['a','b', 2.5, 1, True]
amazon_cart = ['notebook', 'smartphone' , 'book', 'apple', 'cable', 'toy']


amazon_cart[0] = 'laptop'
print(amazon_cart)

#list slicing creates new list!
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(amazon_cart[0::1])
print(amazon_cart)
print(new_cart)