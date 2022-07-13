total = 0
def count():
    global total 
    total += 1
    return total

print(count())


## dependency injection

total = 0
def count(total):
    total += 1
    return total

print(count(total))
# 3 times!
print(count(count(count(total))))