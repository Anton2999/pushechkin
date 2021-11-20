def season(month):
    if month in range(1, 3):
        print("Зима")
    elif month == 12:
        print("Зима")
    elif month in range(3, 6):
        print("Весна")
    elif month in range(6, 9):
        print("Лето")
    elif month in range(9, 12):
        print("Осень")


month = int(input("Введите номер месяца:"))
season(month)
