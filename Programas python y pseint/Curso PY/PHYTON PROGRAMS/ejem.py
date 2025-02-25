import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definir la matriz de rotación
def matriz_rotacion(theta, horario=True):
    if horario:
        return np.array([[np.cos(theta), np.sin(theta)],
                         [-np.sin(theta), np.cos(theta)]])
    else:
        return np.array([[np.cos(theta), -np.sin(theta)],
                         [np.sin(theta), np.cos(theta)]])

# Función para actualizar el gráfico
def update(frame):
    global vector
    theta = np.radians(1)  # Rotar 1 grado por frame
    vector = np.dot(matriz_rotacion(theta, horario), vector)
    line.set_data([0, vector[0]], [0, vector[1]])
    return line,

# Configuración inicial del vector y la figura
vector = np.array([1, 0])
horario = False  # Cambiar a True para rotación horaria
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-', linewidth=2)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Crear la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 360), interval=50, blit=True)

plt.show()