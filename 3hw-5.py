z = input()
b = list()
while z != '':
    b.append(z)
    z = input()
print(b)


b = [float(i) for i in b]    # Преобразуем все элементы списка во float.
middle = sum(b) / len(b)
print(middle)
