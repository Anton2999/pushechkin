from hw31 import spisok


print("Введите список >> ")
a = spisok()
print("Элемент | Частота")
for i in set(a):
    b = a.count(i)
    print(i, "|", b)
