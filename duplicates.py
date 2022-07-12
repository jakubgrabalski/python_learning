some_list = ['a','b','c','d','e','f','g','g','f']
duplicate = []

for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate: 
            duplicate.append(item)

print(duplicate)