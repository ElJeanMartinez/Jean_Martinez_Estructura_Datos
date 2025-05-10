import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Algoritmos de ordenamiento con visualización paso a paso
def bubble_sort(data):
    arr = data[:]
    pasos = ["Inicio: " + str(arr)]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            pasos.append(f"Comparando {arr[j]} y {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                pasos.append(f"Intercambio: {arr}")
            else:
                pasos.append("No se requiere intercambio")
    pasos.append("Lista ordenada: " + str(arr))
    return arr, pasos


def selection_sort(data):
    arr = data[:]
    pasos = ["Inicio: " + str(arr)]
    for i in range(len(arr)):
        min_idx = i
        pasos.append(f"\nBuscando mínimo desde posición {i}")
        for j in range(i+1, len(arr)):
            pasos.append(f"Comparando {arr[min_idx]} con {arr[j]}")
            if arr[min_idx] > arr[j]:
                min_idx = j
                pasos.append(f"Nuevo mínimo encontrado: {arr[min_idx]} en posición {min_idx}")
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            pasos.append(f"Intercambio de {arr[min_idx]} con {arr[i]}: {arr}")
        else:
            pasos.append("No se requiere intercambio")
    pasos.append("Lista ordenada: " + str(arr))
    return arr, pasos


def quicksort_visual(arr):
    pasos = []

    def quicksort_helper(arr, depth=0):
        indent = "  " * depth
        if len(arr) <= 1:
            pasos.append(f"{indent}Lista de un solo elemento o vacía: {arr}")
            return arr
        pivot = arr[0]
        pasos.append(f"{indent}Usando {pivot} como pivote")
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        pasos.append(f"{indent}Izquierda: {left}, Derecha: {right}")
        return quicksort_helper(left, depth + 1) + [pivot] + quicksort_helper(right, depth + 1)

    resultado = quicksort_helper(arr[:])
    pasos.append("Lista ordenada: " + str(resultado))
    return resultado, pasos

# Procesar datos de entrada
def procesar_entrada():
    try:
        datos = list(map(int, entry.get().split(",")))
        return datos
    except:
        messagebox.showerror("Error", "Ingresa números separados por comas (ej. 4,2,9,1)")
        return None

# Funciones de los botones
def ordenar_burbuja():
    datos = procesar_entrada()
    if datos:
        resultado, pasos = bubble_sort(datos)
        output_label.configure(text=f"Resultado: {resultado}")
        mostrar_pasos(pasos)

def ordenar_seleccion():
    datos = procesar_entrada()
    if datos:
        resultado, pasos = selection_sort(datos)
        output_label.configure(text=f"Resultado: {resultado}")
        mostrar_pasos(pasos)

def ordenar_quicksort():
    datos = procesar_entrada()
    if datos:
        resultado, pasos = quicksort_visual(datos)
        output_label.configure(text=f"Resultado: {resultado}")
        mostrar_pasos(pasos)

# Mostrar pasos en el TextBox
def mostrar_pasos(pasos):
    text_box.configure(state="normal")
    text_box.delete("1.0", "end")
    for paso in pasos:
        text_box.insert("end", paso + "\n")
    text_box.configure(state="disabled")

# Interfaz gráfica
app = ctk.CTk()
app.title("Métodos de Ordenamiento - Visualización Paso a Paso")
app.geometry("700x550")

titulo = ctk.CTkLabel(app, text="Taller de Métodos de Ordenamiento", font=("Arial", 20))
titulo.pack(pady=10)

entry = ctk.CTkEntry(app, width=500, placeholder_text="Ingresa números separados por comas")
entry.pack(pady=10)

# Botones
boton_burbuja = ctk.CTkButton(app, text="Método Burbuja", command=ordenar_burbuja)
boton_burbuja.pack(pady=5)

boton_seleccion = ctk.CTkButton(app, text="Método Selección", command=ordenar_seleccion)
boton_seleccion.pack(pady=5)

boton_quick = ctk.CTkButton(app, text="Método Quicksort", command=ordenar_quicksort)
boton_quick.pack(pady=5)

output_label = ctk.CTkLabel(app, text="Resultado: ", font=("Arial", 16))
output_label.pack(pady=10)

# Caja de texto para mostrar pasos
text_box = ctk.CTkTextbox(app, width=600, height=200)
text_box.pack(pady=10)
text_box.configure(state="disabled")

boton_salir = ctk.CTkButton(app, text="Salir", command=app.destroy, fg_color="red", hover_color="darkred")
boton_salir.pack(pady=10)

app.mainloop()
