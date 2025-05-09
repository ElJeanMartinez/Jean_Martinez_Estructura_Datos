# lista_circular.py
from nodo import Nodo

class ListaCircularClientes:
    def __init__(self):
        self.Inicio = None

    def insertar_cliente(self, cedula, nombre): # Funciona como insertar al final/derecha
        nueva = Nodo(cedula, nombre)
        if self.Inicio is None:
            self.Inicio = nueva
            self.Inicio.siguiente = self.Inicio
            # print(f"Cliente {nombre} insertado. La lista estaba vacía. Inicio apunta a {self.Inicio.nombre}.")
        else:
            nueva.siguiente = self.Inicio.siguiente
            self.Inicio.siguiente = nueva
            self.Inicio = nueva
            # print(f"Cliente {nombre} insertado. Inicio ahora apunta a {self.Inicio.nombre}.")
        return True # Indicar éxito

    def listar_clientes_derecha(self):
        if self.Inicio is None:
            return [] # Retornar lista vacía para facilitar el manejo en GUI

        clientes_lista = []
        actual = self.Inicio.siguiente
        primero_visitado = actual
        while True:
            clientes_lista.append(actual) # Guardamos el nodo completo o un string formateado
            actual = actual.siguiente
            if actual == primero_visitado:
                break
        return clientes_lista

    def listar_clientes_izquierda(self):
        if self.Inicio is None:
            return []

        # Obtenemos la lista en orden "derecha" y la invertimos
        lista_derecha = self.listar_clientes_derecha()
        return lista_derecha[::-1] # Invierte la lista

    def eliminar_derecha(self): # Elimina el "primer" elemento lógico (Inicio.siguiente)
        if self.Inicio is None:
            return "La lista está vacía. No se puede eliminar."

        nodo_a_eliminar_nombre = self.Inicio.siguiente.nombre

        if self.Inicio == self.Inicio.siguiente: # Solo hay un nodo
            self.Inicio = None
        else:
            # El último nodo (Inicio) ahora debe apuntar al que sigue del que se elimina
            self.Inicio.siguiente = self.Inicio.siguiente.siguiente
        
        return f"Cliente '{nodo_a_eliminar_nombre}' (primero en lista) eliminado."

    def _encontrar_penultimo(self):
        """
        Helper para encontrar el nodo anterior a self.Inicio.
        Necesario para eliminar_izquierda si Inicio es el que se va.
        """
        if not self.Inicio or self.Inicio.siguiente == self.Inicio:
            return None # No hay penúltimo si la lista está vacía o tiene un solo nodo

        actual = self.Inicio.siguiente
        while actual.siguiente != self.Inicio:
            actual = actual.siguiente
        return actual

    def eliminar_izquierda(self): # Elimina el "último" elemento lógico (el nodo Inicio)
        if self.Inicio is None:
            return "La lista está vacía. No se puede eliminar."

        nodo_a_eliminar_nombre = self.Inicio.nombre

        if self.Inicio == self.Inicio.siguiente: # Solo hay un nodo
            self.Inicio = None
        else:
            penultimo = self._encontrar_penultimo()
            if penultimo: # Debería existir si hay más de un nodo
                penultimo.siguiente = self.Inicio.siguiente # El penúltimo ahora apunta al primero
                self.Inicio = penultimo # El penúltimo se convierte en el nuevo último (Inicio)
            else:
                # Esto no debería ocurrir si hay más de un nodo, pero es una salvaguarda
                return "Error al encontrar el nodo penúltimo."

        return f"Cliente '{nodo_a_eliminar_nombre}' (último en lista) eliminado."