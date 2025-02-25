import matplotlib.pyplot as plt
from fractions import Fraction
'creacion de la matriz y formula para el area'
def d(m):
    return m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] - m[0][2] * m[1][1] * m[2][0] - m[0][0] * m[1][2] * m[2][1] - m[0][1] * m[1][0] * m[2][2]
def ca(x1, y1, x2, y2, x3, y3):
    m = [
        [x1, y1, 1],
        [x2, y2, 1],
        [x3, y3, 1]
    ]
    a = d(m) / 2
    return a
'coordenadas de datos'
print("Introduce las coordenadas del punto A:")
x1, y1 = map(int, input("x1, y1: ").split(','))
print("Introduce las coordenadas del punto B:")
x2, y2 = map(int, input("x2, y2: ").split(','))
print("Introduce las coordenadas del punto C:")
x3, y3 = map(int, input("x3, y3: ").split(','))
'resultado en fraccion'
a = ca(x1, y1, x2, y2, x3, y3)
ar = abs(a)
af = Fraction(ar).limit_denominator()
ad = float(af)
'lineas rojas'
plt.plot([x1, x1], [y1, 0], 'r--')
plt.plot([x2, x2], [y2, 0], 'r--')
plt.plot([x3, x3], [y3, 0], 'r--')
plt.plot([x1, 0], [y1, y1], 'r--')
plt.plot([x2, 0], [y2, y2], 'r--')
plt.plot([x3, 0], [y3, y3], 'r--')

plt.plot([-4, 4], [0, 0], 'b--')
plt.plot([0, 0], [-4, 4], 'b--')

plt.plot([x1, x2], [y1, y2], 'r--')
plt.plot([x2, x3], [y2, y3], 'r--')
plt.plot([x3, x1], [y3, y1], 'r--')
'triangulo'
x_values = [x1, x2, x3, x1]
y_values = [y1, y2, y3, y1]
plt.plot(x_values, y_values, 'k-')

plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'bo-')
plt.fill([x1, x2, x3], [y1, y2, y3], color='lightgray')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triángulo con Área')
plt.grid(True)
plt.axis('equal')
plt.show()
'resultados'
print("El área del triángulo como fracción es:", af)
print("El área del triángulo como número decimal es:", ad)