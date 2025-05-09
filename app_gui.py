import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, Toplevel, scrolledtext
from lista_circular import ListaCircularClientes

class AppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Clientes - Lista Circular Avanzada")
        self.master.geometry("650x450")

        self.lista_clientes = ListaCircularClientes()

        # Tema y contenedor principal
        self.frame = ttk.Frame(master, padding=20)
        self.frame.pack(fill=BOTH, expand=True)

        # --- Sección de Inserción ---
        ttk.Label(self.frame, text="Cédula:", font=("Segoe UI", 11)).grid(row=0, column=0, sticky=W, pady=5)
        self.entry_cedula = ttk.Entry(self.frame, width=30)
        self.entry_cedula.grid(row=0, column=1, columnspan=2, sticky=EW, padx=5)

        ttk.Label(self.frame, text="Nombre:", font=("Segoe UI", 11)).grid(row=1, column=0, sticky=W, pady=5)
        self.entry_nombre = ttk.Entry(self.frame, width=30)
        self.entry_nombre.grid(row=1, column=1, columnspan=2, sticky=EW, padx=5)

        self.btn_insertar = ttk.Button(self.frame, text="Insertar Cliente", bootstyle=SUCCESS, command=self.insertar)
        self.btn_insertar.grid(row=2, column=0, columnspan=3, sticky=EW, pady=(10, 20))

        # --- Sección de Listado ---
        ttk.Label(self.frame, text="Operaciones de Listado:", font=("Segoe UI", 11, "bold")).grid(row=3, column=0, columnspan=3, pady=(5, 0))

        self.btn_listar_derecha = ttk.Button(self.frame, text="Listar Clientes (Derecha)", bootstyle=INFO, command=lambda: self.mostrar_lista_popup("derecha"))
        self.btn_listar_derecha.grid(row=4, column=0, sticky=EW, pady=5, padx=5)

        self.btn_listar_izquierda = ttk.Button(self.frame, text="Listar Clientes (Izquierda)", bootstyle=PRIMARY, command=lambda: self.mostrar_lista_popup("izquierda"))
        self.btn_listar_izquierda.grid(row=4, column=1, sticky=EW, pady=5, padx=5)

        # --- Sección de Eliminación ---
        ttk.Label(self.frame, text="Operaciones de Eliminación:", font=("Segoe UI", 11, "bold")).grid(row=5, column=0, columnspan=3, pady=(10, 0))

        self.btn_eliminar_derecha = ttk.Button(self.frame, text="Eliminar (Derecha/Primero)", bootstyle=WARNING, command=self.eliminar_derecha_gui)
        self.btn_eliminar_derecha.grid(row=6, column=0, sticky=EW, pady=5, padx=5)

        self.btn_eliminar_izquierda = ttk.Button(self.frame, text="Eliminar (Izquierda/Último)", bootstyle=DANGER, command=self.eliminar_izquierda_gui)
        self.btn_eliminar_izquierda.grid(row=6, column=1, sticky=EW, pady=5, padx=5)

        # --- Botón Salir ---
        self.btn_salir = ttk.Button(self.frame, text="Salir", bootstyle=SECONDARY, command=self.master.quit)
        self.btn_salir.grid(row=7, column=0, columnspan=3, pady=20, sticky=EW)

        # Expansión de columnas
        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)

    def insertar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()

        if not cedula or not nombre:
            messagebox.showerror("Error de Validación", "Cédula y Nombre no pueden estar vacíos.")
            return

        if self.lista_clientes.insertar_cliente(cedula, nombre):
            messagebox.showinfo("Éxito", f"Cliente '{nombre}' insertado correctamente.")
            self.entry_cedula.delete(0, ttk.END)
            self.entry_nombre.delete(0, ttk.END)
            self.entry_cedula.focus()
        else:
            messagebox.showerror("Error", "No se pudo insertar el cliente.")

    def mostrar_lista_popup(self, direccion):
        if self.lista_clientes.Inicio is None:
            messagebox.showinfo("Lista Vacía", "No hay clientes para mostrar.")
            return

        if direccion == "derecha":
            lista_nodos = self.lista_clientes.listar_clientes_derecha()
            titulo_popup = "Clientes (Listados hacia la Derecha)"
        elif direccion == "izquierda":
            lista_nodos = self.lista_clientes.listar_clientes_izquierda()
            titulo_popup = "Clientes (Listados hacia la Izquierda)"
        else:
            return

        if not lista_nodos:
            messagebox.showinfo("Lista Vacía", "No hay clientes para mostrar.")
            return

        popup = Toplevel(self.master)
        popup.title(titulo_popup)
        popup.geometry("400x300")

        texto_lista = scrolledtext.ScrolledText(popup, wrap="word", font=("Segoe UI", 10))
        texto_lista.pack(padx=10, pady=10, fill="both", expand=True)

        contenido = [f"Cédula: {nodo.cedula}, Nombre: {nodo.nombre}" for nodo in lista_nodos]
        texto_lista.insert("end", "\n".join(contenido))
        texto_lista.config(state="disabled")

        btn_cerrar_popup = ttk.Button(popup, text="Cerrar", bootstyle=SECONDARY, command=popup.destroy)
        btn_cerrar_popup.pack(pady=10)

    def eliminar_derecha_gui(self):
        resultado = self.lista_clientes.eliminar_derecha()
        messagebox.showinfo("Eliminar Derecha", resultado)

    def eliminar_izquierda_gui(self):
        resultado = self.lista_clientes.eliminar_izquierda()
        messagebox.showinfo("Eliminar Izquierda", resultado)

if __name__ == "__main__":
    app = ttk.Window(themename="flatly")  # Prueba otros temas como "darkly", "solar", "minty"
    AppGUI(app)
    app.mainloop()
