import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para calcular las posiciones (x, y) en el tiro parabólico
def projectile_motion(t, v0x, v0y, g=9.81):
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    return x, y

# Parámetros del tiro parabólico
v0x = 9  # velocidad inicial en el eje x en m/s
theta = np.arctan(4/3)  # ángulo inicial en radianes (calculado para v0x = 9 y v0y = 12)
total_time = 1.5  # tiempo total de vuelo en segundos
dt = 0.05  # intervalo de tiempo para calcular las posiciones
times = np.arange(0, total_time, dt)

# Velocidad inicial en el eje y
v0y = v0x * np.tan(theta)

# Función de inicialización de la animación
def init():
    line.set_data([], [])
    return line,

# Función de animación
def animate(i):
    x = x_values[:i]
    y = y_values[:i]
    line.set_data(x, y)
    return line,

# Calcular la trayectoria completa del tiro parabólico
x_values, y_values = projectile_motion(times, v0x, v0y)

# Crear la figura y los ejes
fig, ax = plt.subplots()
ax.set_xlim(0, 15)
ax.set_ylim(0, 5)
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Graficar la trayectoria del tiro parabólico
line, = ax.plot([], [], 'b-')

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=len(x_values), interval=50, blit=True)

# Mostrar la animación
plt.show()