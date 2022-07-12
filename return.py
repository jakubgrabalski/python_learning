from json import tool


def sum(num1, num2):
    return num1+num2
#print(sum(5,4))

total = sum(10,5)
print(sum(10,total))


def sum(num1, num2):
    def another_sum(n1, n2):
        return n1+n2
    return another_sum(num1, num2)

total = sum(10,20)
print(total)
