import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Colores para cada figura
colors = {
    "circunferencia": "blue",
    "cicloide": "green",
    "hipocicloide": "red",
    "astroide": "orange",
    "lemniscata": "purple",
    "cardioide": "cyan"
}

# Función para crear las curvas paramétricas
def get_parametric_curve(t, curve_type):
    if curve_type == "circunferencia":
        x = np.cos(t)
        y = np.sin(t)
    elif curve_type == "cicloide":
        x = t - np.sin(t)
        y = 1 - np.cos(t)
    elif curve_type == "hipocicloide":
        R, r = 5, 3  # Parámetros de la hipocicloide
        x = (R - r) * np.cos(t) + r * np.cos((R - r) / r * t)
        y = (R - r) * np.sin(t) - r * np.sin((R - r) / r * t)
    elif curve_type == "astroide":
        x = np.cos(t)**3
        y = np.sin(t)**3
    elif curve_type == "lemniscata":
        x = np.cos(t) / (1 + np.sin(t)**2)
        y = np.cos(t) * np.sin(t) / (1 + np.sin(t)**2)
    elif curve_type == "cardioide":
        x = 2 * (1 - np.cos(t)) * np.cos(t)
        y = 2 * (1 - np.cos(t)) * np.sin(t)
    return x, y

# Configurar el gráfico
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_title('Curvas Paramétricas')

# Función para actualizar el gráfico en cada fotograma
def animate(i, t, curve_type):
    x, y = get_parametric_curve(t[:i], curve_type)
    line.set_data(x, y)
    return line,

# Función para inicializar la animación
def init():
    line.set_data([], [])
    return line,

# Crear la ventana de tkinter
root = tk.Tk()
root.title("Animación de Figuras Paramétricas")

# Variable para guardar la animación actual
current_animation = None

# Crear el frame para los gráficos
frame_graph = tk.Frame(root)
frame_graph.grid(row=0, column=0, padx=10, pady=10)

# Insertar el gráfico de matplotlib en tkinter
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.get_tk_widget().pack()

# Crear la función de animación para cada curva
def start_animation(curve_type):
    global current_animation
    # Detener la animación anterior si existe
    if current_animation:
        current_animation.event_source.stop()
    
    # Cambiar el color de la línea a la del tipo de curva
    line.set_color(colors[curve_type])
    
    # Iniciar la nueva animación con mayor velocidad
    t = np.linspace(0, 2 * np.pi, 500)
    current_animation = FuncAnimation(fig, animate, init_func=init, fargs=(t, curve_type),
                                      frames=len(t), interval=30, blit=True)  # Hacer más rápida la animación (intervalo reducido)
    canvas.draw()

# Función para manejar la selección de checkbox
def on_select():
    if var_circunferencia.get():
        start_animation("circunferencia")
    elif var_cicloide.get():
        start_animation("cicloide")
    elif var_hipocicloide.get():
        start_animation("hipocicloide")
    elif var_astroide.get():
        start_animation("astroide")
    elif var_lemniscata.get():
        start_animation("lemniscata")
    elif var_cardioide.get():
        start_animation("cardioide")

# Crear el frame para los checkboxes
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=0, column=1, padx=10, pady=10)

# Crear variables de tkinter para los checkboxes
var_circunferencia = tk.BooleanVar()
var_cicloide = tk.BooleanVar()
var_hipocicloide = tk.BooleanVar()
var_astroide = tk.BooleanVar()
var_lemniscata = tk.BooleanVar()
var_cardioide = tk.BooleanVar()

# Función para resetear los checkboxes al seleccionar uno nuevo
def reset_checkboxes(selected_var):
    var_circunferencia.set(False)
    var_cicloide.set(False)
    var_hipocicloide.set(False)
    var_astroide.set(False)
    var_lemniscata.set(False)
    var_cardioide.set(False)
    selected_var.set(True)

# Añadir checkboxes con colores para cada figura usando tk.Checkbutton
checkbox_circunferencia = tk.Checkbutton(frame_buttons, text="Circunferencia", variable=var_circunferencia,
                                          command=lambda: [reset_checkboxes(var_circunferencia), on_select()])
checkbox_circunferencia.pack(pady=5)
checkbox_circunferencia.config(fg=colors["circunferencia"])

checkbox_cicloide = tk.Checkbutton(frame_buttons, text="Cicloide", variable=var_cicloide,
                                    command=lambda: [reset_checkboxes(var_cicloide), on_select()])
checkbox_cicloide.pack(pady=5)
checkbox_cicloide.config(fg=colors["cicloide"])

checkbox_hipocicloide = tk.Checkbutton(frame_buttons, text="Hipocicloide", variable=var_hipocicloide,
                                        command=lambda: [reset_checkboxes(var_hipocicloide), on_select()])
checkbox_hipocicloide.pack(pady=5)
checkbox_hipocicloide.config(fg=colors["hipocicloide"])

checkbox_astroide = tk.Checkbutton(frame_buttons, text="Astroide", variable=var_astroide,
                                    command=lambda: [reset_checkboxes(var_astroide), on_select()])
checkbox_astroide.pack(pady=5)
checkbox_astroide.config(fg=colors["astroide"])

checkbox_lemniscata = tk.Checkbutton(frame_buttons, text="Lemniscata", variable=var_lemniscata,
                                      command=lambda: [reset_checkboxes(var_lemniscata), on_select()])
checkbox_lemniscata.pack(pady=5)
checkbox_lemniscata.config(fg=colors["lemniscata"])

checkbox_cardioide = tk.Checkbutton(frame_buttons, text="Cardioide", variable=var_cardioide,
                                     command=lambda: [reset_checkboxes(var_cardioide), on_select()])
checkbox_cardioide.pack(pady=5)
checkbox_cardioide.config(fg=colors["cardioide"])

# Ejecutar la interfaz gráfica
root.mainloop()
