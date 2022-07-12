i = 0
while i <= 50:
    print(i)
    i = i + 1 # or i += 1
else:
    print('Done \n')


my_list = [1,2,3]
for item in my_list:
    print(item)

# while - when condition met
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    

while True:
    response = input('Say something: ')
    if (response == 'bye'):
        break