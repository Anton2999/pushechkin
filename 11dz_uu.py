class Fraction:
        def __init__(self, top=0, bottom=1):
            self.num = top
            self.den = bottom

        def input(self): 
            self.num = int(input("Введите числитель: "))
            self.den = int(input("Введите знаменатель: "))
            if self.den == 0:
                Zero Divizion Error("error")
                
        def __str__(self):
            return f"{self.num}/{self.den}"

a1 = Fraction()
print(a1)

a2 = Fraction(3, 4)
print(a2)

a3 = Fraction()
a3.input()
print(a3)
