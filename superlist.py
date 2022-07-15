class SuperList(list):
    def __len__(self):
        return 1000

sl1 = SuperList()

print(len(sl1))
print(sl1.append(5))
print(sl1[0])


print(issubclass(SuperList, list))
print(issubclass(SuperList, object))