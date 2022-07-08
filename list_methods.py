basket = [1, 3, 4, 6, 5, 0]
print(len(basket))
# adding
basket.append(100)
basket.insert(4, 1)
basket.extend([100, 101, 102])
print(basket)

# removing
basket.pop()
basket.pop(1)
basket.remove(4)
#basket.clear()
print(basket)
# shows index when value is found!
print(basket.index(1))
# shows bool value when value is found!
print(1 in basket)
print('x' in basket)
# how many times value is in the basket
print(basket.count(1))
basket1 = basket[:]
basket2 = basket.copy()
basket.sort()
basket2.reverse()
print(basket)
print(basket1)
print(sorted(basket1))
print(basket2)
