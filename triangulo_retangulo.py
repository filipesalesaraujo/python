import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        lados = sorted([self.a, self.b, self.c])
        return math.isclose(lados[0]**2 + lados[1]**2, lados[2]**2)

# Exemplo de uso:
t = Triangulo(1, 3, 5)
print(t.retangulo())  # False

u = Triangulo(3, 4, 5)
print(u.retangulo())  # True
