
class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None # Inicialmente, el siguiente no está definido

    def __str__(self): # Para facilitar la impresión del nodo
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}"