d = [1, 9, 2, 8, 3, 7, 4, 6, 5]
d = sorted(d)
def search(d, n):
    lower = 0
    upper = len(d) - 1
    while lower <= upper:
        center = (lower + upper) // 2
        if d[center] == n:
            return center
        elif d[center] > n:
            upper = center - 1
        elif d[center] < n:
            lower = center + 1
    return None
n = int(input("элемент: "))
print(search(d, n))
assert search([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert search([7, 11, 15, 19, 22, 33, 45], 7) == 0
assert search([], 1) == 'Список пуст'
assert search([5, 5, 10, 15], 5) == 0
assert search([1, 2, 3, 4, 5, 6], 10) == None
