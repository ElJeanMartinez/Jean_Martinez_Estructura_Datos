import customtkinter as ctk
from collections import deque
import tkinter as tk
from tkinter import messagebox

class Bicola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return not self.items

    def insertar_derecha(self, item):
        self.items.append(item)

    def insertar_izquierda(self, item):
        self.items.appendleft(item)

    def atender_derecha(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def atender_izquierda(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None

    def listar(self):
        return list(self.items)

class AppBicola(ctk.CTk):
    def __init__(self, bicola_obj):
        super().__init__()

        self.bicola = bicola_obj
        self.title("Gestor de Bicola Moderno")
        self.geometry("650x550")
        self.resizable(False, False)

        # Colores pastel azulados
        self.color_fondo = "#E0F7FA"
        self.color_frames = "#B2EBF2"
        self.color_botones = "#80DEEA"
        self.color_botones_hover = "#4DD0E1"
        self.color_texto_botones = "#004D40"
        self.color_texto_principal = "#006064"
        self.color_entry_bg = "#FFFFFF"

        ctk.set_appearance_mode("light")
        self.configure(fg_color=self.color_fondo)

        self.label_titulo = ctk.CTkLabel(self, text="Bicola Interactiva",
                                         font=ctk.CTkFont(size=28, weight="bold"),
                                         text_color=self.color_texto_principal)
        self.label_titulo.pack(pady=(20, 10))

        # --- Entrada de datos ---
        self.frame_entrada = ctk.CTkFrame(self, fg_color=self.color_frames, corner_radius=15)
        self.frame_entrada.pack(pady=10, padx=20, fill="x")

        self.entry_nombre = ctk.CTkEntry(self.frame_entrada, placeholder_text="Nombre",
                                         width=150, font=ctk.CTkFont(size=14),
                                         fg_color=self.color_entry_bg, border_color=self.color_botones)
        self.entry_nombre.pack(side="left", padx=5, pady=10)

        self.entry_cedula = ctk.CTkEntry(self.frame_entrada, placeholder_text="Cédula",
                                         width=100, font=ctk.CTkFont(size=14),
                                         fg_color=self.color_entry_bg, border_color=self.color_botones)
        self.entry_cedula.pack(side="left", padx=5, pady=10)

        self.entry_edad = ctk.CTkEntry(self.frame_entrada, placeholder_text="Edad",
                                       width=80, font=ctk.CTkFont(size=14),
                                       fg_color=self.color_entry_bg, border_color=self.color_botones)
        self.entry_edad.pack(side="left", padx=5, pady=10)

        # --- Botones de inserción ---
        self.frame_insercion = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_insercion.pack(pady=5, padx=20, fill="x")

        self.btn_insertar_izquierda = ctk.CTkButton(self.frame_insercion, text="Insertar Izquierda",
                                                    command=self.insertar_izquierda,
                                                    fg_color=self.color_botones,
                                                    hover_color=self.color_botones_hover,
                                                    text_color=self.color_texto_botones,
                                                    font=ctk.CTkFont(size=14, weight="bold"),
                                                    corner_radius=10)
        self.btn_insertar_izquierda.pack(side="left", padx=5, pady=5, expand=True, fill="x")

        self.btn_insertar_derecha = ctk.CTkButton(self.frame_insercion, text="Insertar Derecha",
                                                  command=self.insertar_derecha,
                                                  fg_color=self.color_botones,
                                                  hover_color=self.color_botones_hover,
                                                  text_color=self.color_texto_botones,
                                                  font=ctk.CTkFont(size=14, weight="bold"),
                                                  corner_radius=10)
        self.btn_insertar_derecha.pack(side="left", padx=5, pady=5, expand=True, fill="x")

        # --- Botones de atención ---
        self.frame_atencion = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_atencion.pack(pady=5, padx=20, fill="x")

        self.btn_atender_izquierda = ctk.CTkButton(self.frame_atencion, text="Atender Izquierda",
                                                   command=self.atender_izquierda,
                                                   fg_color=self.color_botones,
                                                   hover_color=self.color_botones_hover,
                                                   text_color=self.color_texto_botones,
                                                   font=ctk.CTkFont(size=14, weight="bold"),
                                                   corner_radius=10)
        self.btn_atender_izquierda.pack(side="left", padx=5, pady=5, expand=True, fill="x")

        self.btn_atender_derecha = ctk.CTkButton(self.frame_atencion, text="Atender Derecha",
                                                 command=self.atender_derecha,
                                                 fg_color=self.color_botones,
                                                 hover_color=self.color_botones_hover,
                                                 text_color=self.color_texto_botones,
                                                 font=ctk.CTkFont(size=14, weight="bold"),
                                                 corner_radius=10)
        self.btn_atender_derecha.pack(side="left", padx=5, pady=5, expand=True, fill="x")

        # --- Botón Mostrar Estado ---
        self.btn_mostrar = ctk.CTkButton(self, text="Mostrar Estado Bicola",
                                         command=self.mostrar_estado_bicola,
                                         fg_color="#AED581", hover_color="#9CCC65",
                                         text_color="#33691E", font=ctk.CTkFont(size=14, weight="bold"),
                                         corner_radius=10)
        self.btn_mostrar.pack(pady=10, padx=150, fill="x")

        # --- Botón Salir ---
        self.btn_salir = ctk.CTkButton(self, text="Salir", command=self.quit,
                                       fg_color="#FF7043", hover_color="#FF5722",
                                       text_color="#FFFFFF",
                                       font=ctk.CTkFont(size=14, weight="bold"),
                                       corner_radius=10)
        self.btn_salir.pack(pady=(5, 20), padx=150, fill="x")

    def insertar_dato(self, lado):
        nombre = self.entry_nombre.get().strip()
        cedula = self.entry_cedula.get().strip()
        edad = self.entry_edad.get().strip()

        if not (nombre and cedula and edad):
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.", parent=self)
            return

        if not edad.isdigit():
            messagebox.showwarning("Advertencia", "Edad debe ser un número.", parent=self)
            return

        registro = {
            "Nombre": nombre,
            "Cédula": cedula,
            "Edad": int(edad)
        }

        if lado == "izquierda":
            self.bicola.insertar_izquierda(registro)
        else:
            self.bicola.insertar_derecha(registro)

        messagebox.showinfo("Éxito", f"Registro insertado por la {lado}.", parent=self)
        self.entry_nombre.delete(0, "end")
        self.entry_cedula.delete(0, "end")
        self.entry_edad.delete(0, "end")

    def insertar_izquierda(self):
        self.insertar_dato("izquierda")

    def insertar_derecha(self):
        self.insertar_dato("derecha")

    def atender_izquierda(self):
        if self.bicola.esta_vacia():
            messagebox.showwarning("Advertencia", "La bicola está vacía.", parent=self)
            return
        atendido = self.bicola.atender_izquierda()
        messagebox.showinfo("Atendido", f"Atendido por la izquierda:\n\n{self.formatear_registro(atendido)}", parent=self)

    def atender_derecha(self):
        if self.bicola.esta_vacia():
            messagebox.showwarning("Advertencia", "La bicola está vacía.", parent=self)
            return
        atendido = self.bicola.atender_derecha()
        messagebox.showinfo("Atendido", f"Atendido por la derecha:\n\n{self.formatear_registro(atendido)}", parent=self)

    def formatear_registro(self, reg):
        return f"Nombre: {reg['Nombre']}\nCédula: {reg['Cédula']}\nEdad: {reg['Edad']}"

    def mostrar_estado_bicola(self):
        ventana = tk.Toplevel(self)
        ventana.title("Estado Actual de la Bicola")
        ventana.geometry("600x400")
        ventana.configure(bg="#E3F2FD")

        label = tk.Label(ventana, text=(
        "Una **bicola** (o doble cola) es una estructura de datos que permite insertar y eliminar "
        "elementos tanto por el lado izquierdo como por el derecho.\n"
        "⬅️ Insertar / Atender por la izquierda     ➡️ Insertar / Atender por la derecha\n\n"
        "Estado actual:"
        ), font=("Arial", 12), bg="#E3F2FD", fg="#0D47A1", justify="left")
        label.pack(padx=15, pady=10, anchor="w")

    # Primer cuadro: Vista esquema
        frame_esquema = tk.Text(ventana, wrap="word", font=("Courier", 12),
                          bg="white", fg="#1A237E", relief="solid", bd=2, height=6)
        frame_esquema.pack(expand=False, fill="x", padx=15, pady=5)

        datos = self.bicola.listar()
        if not datos:
            frame_esquema.insert("end", "\n[ 🟦 Bicola vacía ]")
        else:
            frame_esquema.insert("end", "\nESQUEMA:\n\n")
            frame_esquema.insert("end", "IZQ ⬅️  |  ")

            for i, reg in enumerate(datos):
                formateado = f"[{reg['Nombre']}, {reg['Cédula']}, {reg['Edad']} años]"
                frame_esquema.insert("end", formateado)
                if i < len(datos) - 1:
                    frame_esquema.insert("end", "  <-->  ")

            frame_esquema.insert("end", "  | ➡️ DER\n")

        frame_esquema.config(state="disabled")

    # Segundo cuadro: Vista lista detallada
        frame_lista = tk.Text(ventana, wrap="word", font=("Courier", 12),
                          bg="white", fg="#1A237E", relief="solid", bd=2)
        frame_lista.pack(expand=True, fill="both", padx=15, pady=5)

        frame_lista.insert("end", "LISTA DETALLADA:\n\n")
        if not datos:
            frame_lista.insert("end", "No hay elementos en la bicola.")
        else:
            for i, reg in enumerate(datos, 1):
                frame_lista.insert("end", f"{i}. Nombre: {reg['Nombre']}, Cédula: {reg['Cédula']}, Edad: {reg['Edad']} años\n")

        frame_lista.config(state="disabled")


# --- Ejecutar la aplicación ---
if __name__ == "__main__":
    bicola_actual = Bicola()
    app = AppBicola(bicola_actual)
    app.mainloop()
