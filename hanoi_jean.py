import customtkinter as ctk
import time
import threading
from tkinter import messagebox 

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

BACKGROUND_COLOR = "#EAF6FF"
TOWER_COLOR = "#A3D2CA"
DISK_COLORS = ["#5EAAA8", "#80CED7", "#C8E3D4", "#ADE8F4", "#CAF0F8", "#D0F4DE", "#A0C3D2"]
TORRE_NOMBRES = ['A', 'B', 'C']

class HanoiApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Torres de Hanoi")
        self.geometry("1200x700")
        self.configure(bg=BACKGROUND_COLOR)

        self.num_disks = 3
        self.is_paused = False
        self.stop = False
        self.manual_mode = False
        self.movimientos = 0
        self.start_time = None
        self.running_time = False
        self.selected_tower = None

        self.title_label = ctk.CTkLabel(self, text="Torres de Hanoi", font=("Arial Rounded MT Bold", 28), text_color="#003B73")
        self.title_label.pack(pady=10)

        # Control frame
        self.control_frame = ctk.CTkFrame(self, fg_color="white")
        self.control_frame.pack(pady=10)

        self.disc_label = ctk.CTkLabel(self.control_frame, text="Discos:")
        self.disc_label.pack(side="left", padx=5)

        self.disc_entry = ctk.CTkEntry(self.control_frame, width=50)
        self.disc_entry.insert(0, "3")
        self.disc_entry.pack(side="left", padx=5)

        self.start_btn = ctk.CTkButton(self.control_frame, text="Automático", command=self.iniciar_automatico)
        self.start_btn.pack(side="left", padx=5)

        self.manual_btn = ctk.CTkButton(self.control_frame, text="Manual", command=self.iniciar_manual)
        self.manual_btn.pack(side="left", padx=5)

        self.pause_btn = ctk.CTkButton(self.control_frame, text="Pausar", command=self.toggle_pausa)
        self.pause_btn.pack(side="left", padx=5)

        self.reset_btn = ctk.CTkButton(self.control_frame, text="Reiniciar", command=self.reiniciar)
        self.reset_btn.pack(side="left", padx=5)

        self.move_label = ctk.CTkLabel(self, text="Movimientos: 0", font=("Arial", 14), text_color="#003B73")
        self.move_label.pack()

        self.timer_label = ctk.CTkLabel(self, text="Tiempo: 0.0 s", font=("Arial", 14), text_color="#003B73")
        self.timer_label.pack(pady=2)

        # Main frame
        self.main_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)
        self.main_frame.pack(fill="both", expand=True, padx=10)

        self.canvas = ctk.CTkCanvas(self.main_frame, width=700, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack(side="left", padx=10, pady=20)

        self.log_box = ctk.CTkTextbox(self.main_frame, width=230, height=300, corner_radius=10)
        self.log_box.pack(side="left", padx=10)
        self.log_box.insert("end", "📋 Registro de movimientos:\n")
        self.log_box.configure(state="disabled")

        self.tree_box = ctk.CTkTextbox(self.main_frame, width=230, height=300, corner_radius=10)
        self.tree_box.pack(side="left", padx=10)
        self.tree_box.insert("end", "🌳 Vista del árbol recursivo:\n")
        self.tree_box.configure(state="disabled")

        self.towers = [[], [], []]
        self.tower_coords = [(150, 250), (350, 250), (550, 250)]
        self.tower_width = 10
        self.tower_height = 200
        self.disk_height = 20
        self.disk_shapes = []

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.update_timer()

    def iniciar_automatico(self):
        self.manual_mode = False
        self.iniciar()

    def iniciar_manual(self):
        self.manual_mode = True
        self.iniciar()

    def iniciar(self):
        self.stop = False
        self.movimientos = 0
        self.move_label.configure(text="Movimientos: 0")
        self.num_disks = int(self.disc_entry.get())
        self.towers = [list(reversed(range(1, self.num_disks + 1))), [], []]
        self.start_time = time.time()
        self.running_time = True
        self.selected_tower = None

        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.insert("end", "📋 Registro de movimientos:\n")
        self.log_box.configure(state="disabled")

        self.tree_box.configure(state="normal")
        self.tree_box.delete("1.0", "end")
        self.tree_box.insert("end", "🌳 Vista del árbol recursivo:\n")
        self.tree_box.configure(state="disabled")

        self.draw_towers(self.num_disks)
        if not self.manual_mode:
            threading.Thread(target=self.resolver, args=(self.num_disks, 0, 2, 1, 0)).start()

    def draw_towers(self, num_disks):
        self.canvas.delete("all")
        self.disk_shapes = [[] for _ in range(3)]
        for x, y in self.tower_coords:
            self.canvas.create_rectangle(x - self.tower_width//2, y - self.tower_height, x + self.tower_width//2, y, fill=TOWER_COLOR)
        for i, disk in enumerate(self.towers[0]):
            self.add_disk_visual(0, disk, i)

    def add_disk_visual(self, tower_index, size, position):
        x, y = self.tower_coords[tower_index]
        disk_width = 20 + size * 20
        disk_color = DISK_COLORS[(size - 1) % len(DISK_COLORS)]
        rect = self.canvas.create_rectangle(
            x - disk_width // 2, y - (position + 1) * self.disk_height,
            x + disk_width // 2, y - position * self.disk_height,
            fill=disk_color, outline=""
        )
        self.disk_shapes[tower_index].append((size, rect))

    def move_disk(self, from_tower, to_tower):
        if not self.towers[from_tower]:
            messagebox.showwarning("Movimiento inválido", f"La torre {TORRE_NOMBRES[from_tower]} está vacía.")
            return

        disk = self.towers[from_tower][-1]
        if self.towers[to_tower] and self.towers[to_tower][-1] < disk:
            messagebox.showwarning("Movimiento inválido", f"No puedes poner el disco {disk} sobre uno más pequeño.")
            return

        disk = self.towers[from_tower].pop()
        self.towers[to_tower].append(disk)

        size, shape = self.disk_shapes[from_tower].pop()
        self.canvas.delete(shape)
        pos = len(self.towers[to_tower]) - 1
        self.add_disk_visual(to_tower, size, pos)

        self.movimientos += 1
        self.move_label.configure(text=f"Movimientos: {self.movimientos}")
        self.log_movimiento(size, from_tower, to_tower)
        self.verificar_fin_juego()

    def log_movimiento(self, size, from_tower, to_tower):
        self.log_box.configure(state="normal")
        mensaje = f"🔹 Mover disco {size} de {TORRE_NOMBRES[from_tower]} → {TORRE_NOMBRES[to_tower]}\n"
        self.log_box.insert("end", mensaje)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def log_tree(self, msg, nivel):
        self.tree_box.configure(state="normal")
        self.tree_box.insert("end", "│   " * nivel + msg + "\n")
        self.tree_box.see("end")
        self.tree_box.configure(state="disabled")

    def resolver(self, n, origen, destino, auxiliar, nivel):
        if self.stop: return
        self.log_tree(f"resolver({n}, {TORRE_NOMBRES[origen]}, {TORRE_NOMBRES[destino]}, {TORRE_NOMBRES[auxiliar]})", nivel)
        if n == 1:
            self.move_disk(origen, destino)
            time.sleep(0.4)
        else:
            self.resolver(n - 1, origen, auxiliar, destino, nivel + 1)
            self.move_disk(origen, destino)
            time.sleep(0.4)
            self.resolver(n - 1, auxiliar, destino, origen, nivel + 1)

    def toggle_pausa(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.running_time = False
            self.pause_btn.configure(text="Reanudar")
        else:
            self.start_time = time.time() - (self.elapsed_time or 0)
            self.running_time = True
            self.pause_btn.configure(text="Pausar")

    def reiniciar(self):
        self.stop = True
        self.running_time = False
        self.after(300, self.iniciar)

    def update_timer(self):
        if self.running_time:
            self.elapsed_time = time.time() - self.start_time
            self.timer_label.configure(text=f"Tiempo: {self.elapsed_time:.1f} s")
        self.after(100, self.update_timer)

    def on_canvas_click(self, event):
        if not self.manual_mode:
            return
        for i, (x, _) in enumerate(self.tower_coords):
            if abs(event.x - x) < 50:
                if self.selected_tower is None:
                    if self.towers[i]:
                        self.selected_tower = i
                else:
                    self.move_disk(self.selected_tower, i)
                    self.selected_tower = None
                break
    def verificar_fin_juego(self):
        n = self.num_disks
        # Si todos los discos están en torre 1 o 2 (pero NO en la torre 0)
        if len(self.towers[1]) == n or len(self.towers[2]) == n:
            discos_ordenados = sorted(self.towers[1], reverse=True) == self.towers[1] or \
                                sorted(self.towers[2], reverse=True) == self.towers[2]
            if discos_ordenados:
                messagebox.showinfo("¡Felicidades!", f"¡Has completado el juego en {self.movimientos} movimientos!")
                self.detener_cronometro()


if __name__ == "__main__":
    app = HanoiApp()
    app.mainloop()
