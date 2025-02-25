import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import CheckButtons

# Definir los datos para cada función
t_a = np.linspace(-2, 6, 1000)
x_a = np.sqrt(2*t_a + 4)
y_a = 2*t_a + 1

t_b = np.linspace(0, 2*np.pi, 1000)
x_b = 4 * np.cos(t_b)
y_b = 3 * np.sin(t_b)

t_c = np.linspace(0, 10, 1000)
x_c = t_c
y_c = 2*t_c**2 - 3

t_d = np.linspace(0, 10, 1000)
x_d = 3*t_d - 2
y_d = 18*t_d**2 - 24*t_d + 6

t_e = np.linspace(0, 10, 1000)
x_e = 3*np.cos(t_e) + np.cos(3*t_e)
y_e = 3*np.sin(t_e) - np.sin(3*t_e)

# Crear la figura
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3)  # Deja espacio para los botones

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Crear líneas para cada función
line_a, = ax.plot([], [], lw=2, label="Función a")
line_b, = ax.plot([], [], lw=2, label="Función b")
line_c, = ax.plot([], [], lw=2, label="Función c")
line_d, = ax.plot([], [], lw=2, label="Función d")
line_e, = ax.plot([], [], lw=2, label="Función e")

# Añadir una leyenda
ax.legend()

# Función de inicialización para la animación
def init():
    line_a.set_data([], [])
    line_b.set_data([], [])
    line_c.set_data([], [])
    line_d.set_data([], [])
    line_e.set_data([], [])
    return line_a, line_b, line_c, line_d, line_e

# Función de actualización de la animación
def update(frame):
    line_a.set_data(x_a[:frame], y_a[:frame])
    line_b.set_data(x_b[:frame], y_b[:frame])
    line_c.set_data(x_c[:frame], y_c[:frame])
    line_d.set_data(x_d[:frame], y_d[:frame])
    line_e.set_data(x_e[:frame], y_e[:frame])
    return line_a, line_b, line_c, line_d, line_e

# Crear la animación
ani = FuncAnimation(fig, update, frames=1000, init_func=init, interval=20, blit=True)

# Crear los botones para mostrar/ocultar líneas
rax = plt.axes([0.05, 0.4, 0.2, 0.4])  # Posición del panel de botones
labels = ['Función a', 'Función b', 'Función c', 'Función d', 'Función e']
visibility = [True, True, True, True, True]  # Todas las líneas visibles al principio
check = CheckButtons(rax, labels, visibility)

# Función para mostrar/ocultar líneas cuando se presiona un botón
def toggle_visibility(label):
    if label == 'Función a':
        line_a.set_visible(not line_a.get_visible())
    elif label == 'Función b':
        line_b.set_visible(not line_b.get_visible())
    elif label == 'Función c':
        line_c.set_visible(not line_c.get_visible())
    elif label == 'Función d':
        line_d.set_visible(not line_d.get_visible())
    elif label == 'Función e':
        line_e.set_visible(not line_e.get_visible())
    plt.draw()

# Vincular los botones con la función toggle_visibility
check.on_clicked(toggle_visibility)

# Mostrar la animación
plt.show()