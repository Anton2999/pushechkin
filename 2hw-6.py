a = list(input('Введите строку'))
b = []
for i in a:
    if i.isdigit():   # isdigit() возвращает True, если все цифры
        b.append(i)
k = int(input('Введите k'))
print(k, '-ая цифра в строке', b[k-1])
