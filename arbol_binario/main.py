import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext # Para una salida de texto más grande

# --- CLASE NODO ---
class Nodo:
    """
    Representa un nodo individual en el árbol binario de búsqueda.
    Cada nodo contiene un valor, y referencias a sus hijos izquierdo y derecho.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# --- CLASE ARBOL BINARIO DE BÚSQUEDA ---
class ArbolBinarioBusqueda:
    """
    Implementa un Árbol Binario de Búsqueda (BST).
    Maneja las operaciones de inserción y los tres tipos de recorridos (Inorden, Preorden, Postorden).
    """
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """
        Inserta un nuevo valor en el árbol de forma ordenada.
        Si el árbol está vacío, el nuevo valor se convierte en la raíz.
        De lo contrario, se busca la posición correcta recursivamente.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        """
        Función auxiliar recursiva para insertar un valor en el árbol.
        Compara el valor con el nodo_actual para decidir si ir a la izquierda o a la derecha.
        """
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor: # Permite no insertar duplicados o manejarlos si la lógica lo requiere
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
        else:
            # Opcional: Manejar duplicados. Por ahora, simplemente no los insertamos.
            print(f"El valor {valor} ya existe en el árbol.")

    def inorden(self):
        """
        Realiza un recorrido Inorden del árbol.
        Orden: Subárbol Izquierdo, Raíz, Subárbol Derecho.
        Devuelve una cadena con los valores del recorrido.
        """
        valores_inorden = []
        self._inorden_recursivo(self.raiz, valores_inorden)
        return " -> ".join(map(str, valores_inorden))

    def _inorden_recursivo(self, nodo_actual, lista_valores):
        """
        Función auxiliar recursiva para el recorrido Inorden.
        """
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierdo, lista_valores)
            lista_valores.append(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecho, lista_valores)

    def preorden(self):
        """
        Realiza un recorrido Preorden del árbol.
        Orden: Raíz, Subárbol Izquierdo, Subárbol Derecho.
        Devuelve una cadena con los valores del recorrido.
        """
        valores_preorden = []
        self._preorden_recursivo(self.raiz, valores_preorden)
        return " -> ".join(map(str, valores_preorden))

    def _preorden_recursivo(self, nodo_actual, lista_valores):
        """
        Función auxiliar recursiva para el recorrido Preorden.
        """
        if nodo_actual:
            lista_valores.append(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierdo, lista_valores)
            self._preorden_recursivo(nodo_actual.derecho, lista_valores)

    def postorden(self):
        """
        Realiza un recorrido Postorden del árbol.
        Orden: Subárbol Izquierdo, Subárbol Derecho, Raíz.
        Devuelve una cadena con los valores del recorrido.
        """
        valores_postorden = []
        self._postorden_recursivo(self.raiz, valores_postorden)
        return " -> ".join(map(str, valores_postorden))

    def _postorden_recursivo(self, nodo_actual, lista_valores):
        """
        Función auxiliar recursiva para el recorrido Postorden.
        """
        if nodo_actual:
            self._postorden_recursivo(nodo_actual.izquierdo, lista_valores)
            self._postorden_recursivo(nodo_actual.derecho, lista_valores)
            lista_valores.append(nodo_actual.valor)

# --- CLASE DE LA INTERFAZ GRÁFICA ---
class AppArbolBinario:
    """
    Clase principal que gestiona la interfaz gráfica de usuario (GUI)
    y las interacciones con el Árbol Binario de Búsqueda.
    """
    def __init__(self, master):
        """
        Constructor de la aplicación GUI.
        Configura la ventana principal y los widgets.
        """
        self.master = master
        master.title("🌳 Gestor de Árbol Binario de Búsqueda 🌳")
        master.geometry("600x500") # Tamaño inicial de la ventana
        master.resizable(False, False) # Deshabilita el redimensionamiento
        master.config(bg="#f0f0f0") # Color de fondo

        self.arbol = ArbolBinarioBusqueda() # Instancia del árbol binario

        # --- Frames para organizar la interfaz ---
        self.input_frame = tk.Frame(master, bg="#e0e0e0", bd=2, relief="groove", padx=10, pady=10)
        self.input_frame.pack(pady=10, padx=10, fill="x")

        self.button_frame = tk.Frame(master, bg="#e0e0e0", bd=2, relief="groove", padx=10, pady=10)
        self.button_frame.pack(pady=10, padx=10, fill="x")

        self.output_frame = tk.Frame(master, bg="#e0e0e0", bd=2, relief="groove", padx=10, pady=10)
        self.output_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # --- Widgets de Entrada ---
        tk.Label(self.input_frame, text="Valor a insertar:", bg="#e0e0e0", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        self.valor_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 10))
        self.valor_entry.pack(side="left", padx=5)
        self.valor_entry.bind("<Return>", lambda event=None: self.insertar_dato()) # Permite insertar con Enter

        self.insertar_btn = tk.Button(self.input_frame, text="Insertar", command=self.insertar_dato,
                                      bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
        self.insertar_btn.pack(side="left", padx=10)

        # --- Botones de Recorrido ---
        self.inorden_btn = tk.Button(self.button_frame, text="Imprimir Inorden", command=self.imprimir_inorden,
                                     bg="#2196F3", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
        self.inorden_btn.pack(side="left", expand=True, padx=5, pady=5)

        self.preorden_btn = tk.Button(self.button_frame, text="Imprimir Preorden", command=self.imprimir_preorden,
                                      bg="#FFC107", fg="black", font=("Arial", 10, "bold"), relief="raised", bd=3)
        self.preorden_btn.pack(side="left", expand=True, padx=5, pady=5)

        self.postorden_btn = tk.Button(self.button_frame, text="Imprimir Postorden", command=self.imprimir_postorden,
                                       bg="#FF5722", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
        self.postorden_btn.pack(side="left", expand=True, padx=5, pady=5)

        self.salir_btn = tk.Button(self.button_frame, text="Salir", command=master.quit,
                                   bg="#F44336", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
        self.salir_btn.pack(side="left", expand=True, padx=5, pady=5)

        # --- Área de Salida ---
        tk.Label(self.output_frame, text="Resultados del Recorrido:", bg="#e0e0e0", font=("Arial", 10, "bold")).pack(anchor="w", pady=5)
        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, width=60, height=10, font=("Consolas", 10), bg="#ffffff", bd=2, relief="sunken")
        self.output_text.pack(fill="both", expand=True, pady=5)

    def insertar_dato(self):
        """
        Maneja la inserción de un dato en el árbol desde la GUI.
        Valida que la entrada sea un número entero.
        """
        try:
            valor_str = self.valor_entry.get()
            if not valor_str:
                messagebox.showwarning("Entrada Vacía", "Por favor, ingrese un valor.")
                return

            valor = int(valor_str)
            self.arbol.insertar(valor)
            messagebox.showinfo("Éxito", f"'{valor}' insertado correctamente.")
            self.valor_entry.delete(0, tk.END) # Limpia el campo de entrada
            self.actualizar_salida("Dato insertado. Realice un recorrido para ver los cambios.")
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese un número entero válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al insertar: {e}")

    def imprimir_inorden(self):
        """
        Muestra el recorrido Inorden del árbol en el área de salida.
        """
        if self.arbol.raiz is None:
            self.actualizar_salida("El árbol está vacío. No hay nada que imprimir en Inorden.")
        else:
            recorrido = self.arbol.inorden()
            self.actualizar_salida(f"Recorrido Inorden: \n{recorrido}")

    def imprimir_preorden(self):
        """
        Muestra el recorrido Preorden del árbol en el área de salida.
        """
        if self.arbol.raiz is None:
            self.actualizar_salida("El árbol está vacío. No hay nada que imprimir en Preorden.")
        else:
            recorrido = self.arbol.preorden()
            self.actualizar_salida(f"Recorrido Preorden: \n{recorrido}")

    def imprimir_postorden(self):
        """
        Muestra el recorrido Postorden del árbol en el área de salida.
        """
        if self.arbol.raiz is None:
            self.actualizar_salida("El árbol está vacío. No hay nada que imprimir en Postorden.")
        else:
            recorrido = self.arbol.postorden()
            self.actualizar_salida(f"Recorrido Postorden: \n{recorrido}")

    def actualizar_salida(self, texto):
        """
        Actualiza el contenido del área de texto de salida.
        """
        self.output_text.delete(1.0, tk.END) # Borra el contenido actual
        self.output_text.insert(tk.END, texto) # Inserta el nuevo texto

# --- FUNCIÓN PRINCIPAL ---
if __name__ == "__main__":
    # Crea la ventana principal de Tkinter
    root = tk.Tk()
    # Crea una instancia de la aplicación GUI
    app = AppArbolBinario(root)
    # Inicia el bucle principal de la aplicación GUI
    root.mainloop()