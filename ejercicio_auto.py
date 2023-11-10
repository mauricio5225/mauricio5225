# creamos superclase / clase padre
class Vehiculo():
    #construcor de atributos
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas        
    def __str__(self):
        return f"Vehiculo color {self.color} con {self.ruedas} ruedas"
    
    #creamos subclase/clase hijo
class Coche(Vehiculo):                                                                                                                                                   
        def __init__(self, color, ruedas, velocidad, cilindrada):
            # super= a nivel superior
            Vehiculo._init_(self, color, ruedas)
            self.velocidad = velocidad
            self.cilindrada = cilindrada
        def __str__(self):
            return f"{super().__str__()} ,{self.velocidad} km/h + {self.cilindrada} cc"               
                
v = Vehiculo("azul", 4)
print(v)
    
#creamos instancia del Coche

c= Coche("negro", 4,250, 3500)
print(c)