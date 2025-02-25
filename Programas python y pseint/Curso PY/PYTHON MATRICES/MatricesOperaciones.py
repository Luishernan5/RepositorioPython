import numpy as np

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return np.array(matriz)

def mostrar_matriz(nombre, matriz):
    print(f"{nombre}:")
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

def determinante_matriz(matriz):
    try:
        determinante = np.linalg.det(matriz)
        return determinante
    except np.linalg.LinAlgError:
        print("No se puede calcular el determinante de la matriz.")

def main():
    num_matrices = int(input("¿Cuántas matrices se van a calcular? "))
    matrices = {}
    for i in range(num_matrices):
        filas = int(input(f"¿Cuántas filas tiene la matriz {chr(65 + i)}? "))
        columnas = int(input(f"¿Cuántas columnas tiene la matriz {chr(65 + i)}? "))
        matrices[chr(65 + i)] = crear_matriz(filas, columnas)

    print("\nTenemos las matrices:")
    for nombre, matriz in matrices.items():
        mostrar_matriz(nombre, matriz)

    operacion = input("Ingrese la operación a realizar (suma, resta, multiplicacion, escalar, inversion, determinante, transpuesta): ")

    if operacion == "suma" or operacion == "resta":
        matriz1 = matrices[input("Ingrese la letra de la primera matriz: ")]
        matriz2 = matrices[input("Ingrese la letra de la segunda matriz: ")]
        if operacion == "suma":
            resultado = matriz1 + matriz2
            mostrar_matriz("Resultado de la suma", resultado)
        else:
            resultado = matriz1 - matriz2
            mostrar_matriz("Resultado de la resta", resultado)

    elif operacion == "multiplicacion":
        matriz1 = matrices[input("Ingrese la letra de la primera matriz: ")]
        matriz2 = matrices[input("Ingrese la letra de la segunda matriz: ")]
        resultado = np.dot(matriz1, matriz2)
        mostrar_matriz("Resultado de la multiplicación", resultado)

    elif operacion == "escalar":
        matriz = matrices[input("Ingrese la letra de la matriz: ")]
        escalar = float(input("Ingrese el escalar: "))
        resultado = matriz * escalar
        mostrar_matriz("Resultado de la multiplicación escalar", resultado)

    elif operacion == "inversion":
        matriz = matrices[input("Ingrese la letra de la matriz: ")]
        resultado = np.linalg.inv(matriz)
        mostrar_matriz("Resultado de la inversión", resultado)

    elif operacion == "determinante":
        matriz = matrices[input("Ingrese la letra de la matriz: ")]
        determinante = determinante_matriz(matriz)
        print(f"Determinante de {input}: = {determinante}")

    elif operacion == "transpuesta":
        matriz = matrices[input("Ingrese la letra de la matriz: ")]
        transpuesta = np.transpose(matriz)
        mostrar_matriz("Transpuesta de la matriz", transpuesta)

if __name__ == "__main__":
    main()