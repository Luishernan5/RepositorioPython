import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definimos la función para la matriz de rotación
def rot_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], 
                     [np.sin(theta), np.cos(theta)]])

# Configuración inicial del gráfico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
axes = [ax1, ax2]

for ax, label in zip(axes, ['A', 'B']):
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    circle = plt.Circle((0, 0), 1, color='lightgrey', fill=False)
    ax.add_artist(circle)
    ax.text(0, 0, 'A', fontsize=12, ha='center', va='center')
    if ax == ax1:
        point_B1, = ax.plot([1], [0], 'o', color='blue')  # Punto B inicialmente en (1, 0)
        ax.text(1, 0, 'B', fontsize=12, ha='center', va='center')
    elif ax == ax2:
        point_B2, = ax.plot([-1], [0], 'o', color='blue')  # Punto B inicialmente en (-1, 0)
        ax.text(-1, 0, 'B', fontsize=12, ha='center', va='center')

# Vectores iniciales
vector = np.array([1, 0])
vector_plot1, = ax1.plot([0, vector[0]], [0, vector[1]], marker='o')
vector_plot2, = ax2.plot([0, vector[0]], [0, vector[1]], marker='o')

# Función de actualización para la animación
def update(frame):
    theta = np.radians(frame)
    rotation1 = rot_matrix(theta)  # Matriz de rotación para sentido antihorario
    rotation2 = rot_matrix(-theta) # Matriz de rotación para sentido horario
    
    # Actualizar vector en sentido antihorario (ax1)
    rotated_vector1 = rotation1 @ vector
    vector_plot1.set_data([0, rotated_vector1[0]], [0, rotated_vector1[1]])
    point_B1.set_data([rotated_vector1[0]], [rotated_vector1[1]])  # Actualizar posición de B
    
    # Actualizar vector en sentido horario (ax2)
    rotated_vector2 = rotation2 @ vector
    vector_plot2.set_data([0, rotated_vector2[0]], [0, rotated_vector2[1]])
    point_B2.set_data([rotated_vector2[0]], [rotated_vector2[1]])  # Actualizar posición de B
    
    return vector_plot1, vector_plot2, point_B1, point_B2

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=range(0, 360, 5), blit=True)
ax1.set_title('Rotación Antihoraria')
ax2.set_title('Rotación Horaria')

plt.tight_layout()
plt.show()