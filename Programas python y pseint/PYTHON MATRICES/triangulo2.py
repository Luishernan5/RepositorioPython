import matplotlib.pyplot as plt
from fractions import Fraction

def determinante(matriz):
    return matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1] - matriz[0][2] * matriz[1][1] * matriz[2][0] - matriz[0][0] * matriz[1][2] * matriz[2][1] - matriz[0][1] * matriz[1][0] * matriz[2][2]

def calcular_area(x1, y1, x2, y2, x3, y3):
    matriz = [
        [x1, y1, 1],
        [x2, y2, 1],
        [x3, y3, 1]
    ]
    area = determinante(matriz) / 2
    return area

print("Introduce las coordenadas del punto A:")
x1, y1 = map(int, input("x1, y1: ").split(','))
print("Introduce las coordenadas del punto B:")
x2, y2 = map(int, input("x2, y2: ").split(','))
print("Introduce las coordenadas del punto C:")
x3, y3 = map(int, input("x3, y3: ").split(','))

area = calcular_area(x1, y1, x2, y2, x3, y3)

# Convertir el área a fracción irreducible
area_abs = abs(area)
area_fraccion = Fraction(area_abs).limit_denominator()

# Calcular el área como número decimal
area_decimal = float(area_fraccion)

# Líneas punteadas rojas desde cada vértice del triángulo hasta el eje X y el eje Y
plt.plot([x1, x1], [y1, 0], 'r--')
plt.plot([x2, x2], [y2, 0], 'r--')
plt.plot([x3, x3], [y3, 0], 'r--')
plt.plot([x1, 0], [y1, y1], 'r--')
plt.plot([x2, 0], [y2, y2], 'r--')
plt.plot([x3, 0], [y3, y3], 'r--')

# Línea adicional desde el punto A hacia el punto B

# Extensión de la línea hacia arriba
plt.plot([x1, y2], [y1+1, max(x1, y2)], 'g--')

# Líneas que conectan los puntos A, B y C
plt.plot([x1, x2], [y1, y2], 'r--')
plt.plot([x2, x3], [y2, y3], 'r--')
plt.plot([x3, x1], [y3, y1], 'r--')

# Cuadrado que encierra el triángulo
x_values = [x1, x2, x3, x1]
y_values = [y1, y2, y3, y1]
plt.plot(x_values, y_values, 'k-')

# Gráfico del triángulo
plt.fill(x_values, y_values, color='lightgray')
plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'bo-')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triángulo con Área')
plt.grid(True)
plt.axis('equal')
plt.show()

print("El área del triángulo como fracción es:", area_fraccion)
print("El área del triángulo como número decimal es:", area_decimal)