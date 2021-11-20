z = input()
b = list()
while z != '':
    b.append(z)
    z = input()
print(b)

for x in set(b):    # set() - преобразует в множество, удаляя дубликаты.
    y = b.count(x)
    print("Элемент - ", x, "\t|""\tЧастота - ", y)
