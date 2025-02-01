class Triangulo:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self) -> str:
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isósceles"
        else:
            return "escaleno"
