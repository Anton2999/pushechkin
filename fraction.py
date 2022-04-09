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
        return str(self.num)+"/"+str(self.den)


    def reduce_fraction(self):
        k = math.gcd(self.num, self.den)
        self.num = self.num // k
        self.den = self.den // k


k = Fraction(2,4)
print(k)
k.reduce_fraction()
print(k)

a1 = Fraction()
print(a1)

a2 = Fraction(3, 4)
print(a2)

a3 = Fraction()
a3.input()
a3.reduce_fraction()
print(a3)

