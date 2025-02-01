class Triangulo:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self) -> int:
        return self.a + self.b + self.c
