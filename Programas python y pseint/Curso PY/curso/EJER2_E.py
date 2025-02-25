def calcular_serie_potencias(N):
    suma = 0
    for i in range(1, N+1):
        termino = i**(i+1)
        suma += termino
    
    return suma

# Pedir al usuario que ingrese el valor de N
N = int(input("Ingresa un número entero para calcular la serie de potencias: "))
resultado_final = calcular_serie_potencias(N) /N
print("Resultado de la suma de términos:", resultado_final)