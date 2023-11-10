class Cachorro():
    
    def __init__(self, color, raza):
        self.color = color
        self.raza = raza


perrito = Cachorro("Marrón claro", "Golden retriever")

print(perrito)
class Cachorro():
    
    def __init__(self, color, raza):
        self.color = color
        self.raza = raza

    def __str__(self):
        return """\
Raza: {}
Color: {}""".format(self.raza, self.color)


perrito = Cachorro("Marrón claro", "Golden retriever")

print(perrito)