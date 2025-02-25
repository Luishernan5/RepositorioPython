import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Datos iniciales
vx = 9  # Componente de la velocidad en x (m/s)
g = 9.81  # Aceleración debido a la gravedad (m/s^2)
t_total = 1.5  # Tiempo total de simulación (s)
altura_inicial = 20  # Altura inicial desde donde se lanza el proyectil (m)

# Funciones de posición en x e y
x = lambda t: vx * t
y = lambda t: altura_inicial - 0.5 * g * t**2

# Creamos el vector de tiempos para la animación
t = np.linspace(0, t_total, 100)

# Calculamos las posiciones en x e y en cada instante de tiempo
posiciones_x = x(t)
posiciones_y = y(t)

# Inicializamos la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, np.max(posiciones_x) + 1)
ax.set_ylim(0, altura_inicial + 1)
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlabel('Distancia horizontal (m)', fontsize=12)
ax.set_ylabel('Altura vertical (m)', fontsize=12)
ax.set_title('Simulación de Tiro Parabólico', fontsize=14)

# Dibujamos la trayectoria
trayectoria, = ax.plot([], [], 'b-', linewidth=2)

# Inicializamos el punto que recorre la trayectoria
punto, = ax.plot([], [], 'ko', markersize=8)

# Etiqueta de velocidad inicial y tiempo total
info_text = ax.text(0.02, 0.02, '', transform=ax.transAxes, ha='left', va='bottom', fontsize=12)

# Inicializamos los vectores de desplazamiento con etiquetas y puntos iniciales
vector1, = ax.plot([], [], 'r--', linewidth=1)
vector1_label = ax.text(0, 0, 'Vector 1', fontsize=12, color='r', ha='center', va='center')
vector1_start = ax.plot([], [], 'ro', markersize=8)

vector2, = ax.plot([], [], 'b--', linewidth=1)
vector2_label = ax.text(0, 0, 'Vector 2', fontsize=12, color='b', ha='center', va='center')
vector2_start = ax.plot([], [], 'bo', markersize=8)

vector3, = ax.plot([], [], 'g--', linewidth=1)
vector3_label = ax.text(0, 0, 'Vector 3', fontsize=12, color='g', ha='center', va='center')
vector3_start = ax.plot([], [], 'go', markersize=8)

# Función de inicialización de la animación
def init():
    trayectoria.set_data([], [])
    punto.set_data([], [])
    info_text.set_text('')
    vector1.set_data([], [])
    vector1_label.set_position((0, 0))
    vector1_start[0].set_data([], [])
    vector2.set_data([], [])
    vector2_label.set_position((0, 0))
    vector2_start[0].set_data([], [])
    vector3.set_data([], [])
    vector3_label.set_position((0, 0))
    vector3_start[0].set_data([], [])
    return trayectoria, punto, info_text, vector1, vector1_label, vector1_start[0], vector2, vector2_label, vector2_start[0], vector3, vector3_label, vector3_start[0]

# Función de actualización de la animación
def update(frame):
    # Actualizamos la trayectoria hasta el punto actual
    trayectoria.set_data(posiciones_x[:frame], posiciones_y[:frame])
    
    # Actualizamos la posición del punto
    punto.set_data(posiciones_x[frame], posiciones_y[frame])
    
    # Actualizamos los vectores en cada instante de tiempo
    if frame > 0:
        # Etiquetas de velocidad inicial y tiempo total
        info_text.set_text(f'D = {vx} m/s\nT = {t_total} s')
        
        # Posiciones fijas de los vectores y puntos de inicio
        pos_vector1 = (posiciones_x[20], posiciones_y[20])
        pos_vector2 = (posiciones_x[40], posiciones_y[40])
        pos_vector3 = (posiciones_x[60], posiciones_y[60])
        
        # Vector 1
        vector1.set_data([posiciones_x[frame-20], pos_vector1[0]], [posiciones_y[frame-20], pos_vector1[1]])
        vector1_label.set_position((pos_vector1[0] + 1, pos_vector1[1] + 1))
        vector1_start[0].set_data(pos_vector1)
        
        # Vector 2
        vector2.set_data([posiciones_x[frame-40], pos_vector2[0]], [posiciones_y[frame-40], pos_vector2[1]])
        vector2_label.set_position((pos_vector2[0] + 1, pos_vector2[1] + 1))
        vector2_start[0].set_data(pos_vector2)
        
        # Vector 3
        vector3.set_data([posiciones_x[frame-60], pos_vector3[0]], [posiciones_y[frame-60], pos_vector3[1]])
        vector3_label.set_position((pos_vector3[0] + 1, pos_vector3[1] + 1))
        vector3_start[0].set_data(pos_vector3)
    
    return trayectoria, punto, info_text, vector1, vector1_label, vector1_start[0], vector2, vector2_label, vector2_start[0], vector3, vector3_label, vector3_start[0]

# Configuramos la animación
ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

# Mostramos la animación
plt.show()