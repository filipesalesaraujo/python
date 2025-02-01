class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        lados1 = sorted([self.a, self.b, self.c])
        lados2 = sorted([triangulo.a, triangulo.b, triangulo.c])
        return (lados1[0] / lados2[0] == lados1[1] / lados2[1] == lados1[2] / lados2[2])

# Exemplo de uso:
t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
print(t1.semelhantes(t2))  # True
