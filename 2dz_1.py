import fractions
import math


class Fraction:
        def __init__(self, top=0, bottom=1):
            self.num = top
            self.den = bottom

        def input(self): 
            self.num = int(input("Введите числитель: "))
            self.den = int(input("Введите знаменатель: "))
            if self.den == 0:
                raise ZeroDivizionError
                
        def __str__(self):
            return f"{self.num}/{self.den}"
def reduce_fraction(f):
    k = math.gcd(f.num, f.den)
    return Fraction(f.num//k, f.den//k)


k = Fraction()
print(k)

a1 = Fraction()
print(a1)

a2 = Fraction(3, 4)
print(a2)

a3 = Fraction()
a3.input()
print(a3)

