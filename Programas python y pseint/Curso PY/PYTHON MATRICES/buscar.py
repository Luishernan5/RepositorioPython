def ingresar_matriz(nombre):
    matriz = []
    print(f"Ingrese los valores de la matriz {nombre}:")
    filas = int(input(f"Número de filas de la matriz {nombre}: "))
    columnas = int(input(f"Número de columnas de la matriz {nombre}: "))

    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = input(f"Ingrese el valor para la fila {i+1} y la columna {j+1} de la matriz {nombre}: ")
            fila.append(valor)
        matriz.append(fila)
    return matriz

def encontrar_valores_faltantes(matriz_a, matriz_b, matriz_resultado):
    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[0])):
            if matriz_a[i][j] == 'F':
                matriz_a[i][j] = str(int(matriz_resultado[i][j]) - int(matriz_b[i][j]))
            elif matriz_b[i][j] == 'F':
                matriz_b[i][j] = str(int(matriz_resultado[i][j]) - int(matriz_a[i][j]))

def imprimir_matriz(matriz, nombre):
    print(f"\nMatriz {nombre}:")
    for fila in matriz:
        print(" ".join(fila))

def imprimir_suma(matriz_a, matriz_b, matriz_resultado):
    print("\nMatriz A + Matriz B = Matriz Resultado:")
    for i in range(len(matriz_a)):
        fila_suma = []
        for j in range(len(matriz_a[0])):
            if matriz_a[i][j] != 'F' and matriz_b[i][j] != 'F':
                suma = int(matriz_a[i][j]) + int(matriz_b[i][j])
                fila_suma.append(str(suma))
            else:
                fila_suma.append(matriz_resultado[i][j])
        print(" ".join(fila_suma))

# Ingresar las matrices A, B y el resultado
matriz_a = ingresar_matriz("A")
matriz_b = ingresar_matriz("B")
matriz_resultado = ingresar_matriz("Resultado")

# Encontrar los valores faltantes en las matrices A y B
encontrar_valores_faltantes(matriz_a, matriz_b, matriz_resultado)

# Imprimir las matrices A y B
imprimir_matriz(matriz_a, "A")
imprimir_matriz(matriz_b, "B")

# Imprimir la suma de las matrices A y B junto con el resultado
imprimir_suma(matriz_a, matriz_b, matriz_resultado)
