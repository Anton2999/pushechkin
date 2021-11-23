from hw31 import spisok


b = [float(i) for i in spisok()]    # Преобразуем все элементы списка во float.
middle = sum(b) / len(b)
print(middle)
