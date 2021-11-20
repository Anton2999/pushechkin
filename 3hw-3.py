def fibonacci(n):
    F1 = 0
    F2 = 1
    print(F1)
    print(F2)
    for i in range(n-2):
        F1 = F1 + F2
        print(F1)
        F1, F2 = F2, F1


x = fibonacci(int(input("Введите число")))
