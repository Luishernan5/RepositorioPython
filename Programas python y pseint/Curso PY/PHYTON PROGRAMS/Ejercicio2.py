import numpy as np

def verificar_linealmente_independientes(conjunto):
    num_pol = len(conjunto)
    matriz_coeficientes = np.zeros((num_pol, num_pol))
    vector_resultado = np.zeros(num_pol)

    # Construir la matriz de coeficientes y el vector resultado
    for i, polinomio in enumerate(conjunto):
        for j in range(num_pol):
            matriz_coeficientes[i][j] = polinomio[j]
        vector_resultado[i] = -polinomio[-1]

    # Resolver el sistema de ecuaciones
    soluciones = np.linalg.solve(matriz_coeficientes, vector_resultado)

    # Comprobar si todas las soluciones son aproximadamente cero
    independiente = np.allclose(soluciones, np.zeros(num_pol))

    return soluciones, independiente

def mostrar_resultados_letra(letra, conjunto, soluciones, independiente):
    print(f"Para el conjunto {letra}:")
    for polinomio in conjunto:
        print(polinomio)
    print("\nEl sistema de ecuaciones es:\n")
    for i, polinomio in enumerate(conjunto):
        print(f"{polinomio[0]}a + {polinomio[1]}b + {polinomio[2]}c = 0")
    print("\nLos resultados son:")
    for i in range(len(soluciones)):
        print(f"{chr(97 + i)} = {soluciones[i]}")
    if independiente:
        print("\nEsto significa que todos los coeficientes son cero simultáneamente, por lo que los polinomios son linealmente independientes.\n")
    else:
        print("\nEsto significa que no todos los coeficientes son cero simultáneamente, por lo que los polinomios no son linealmente independientes.\n")

# Conjuntos de polinomios
conjunto_a = np.array([[2, -1, 2], [0, 2, -1], [6, -5, 1]])
conjunto_b = np.array([[-1, 0, 1], [5, 2, 0]])
conjunto_c = np.array([[1, 3, 1], [2, 1, -1], [0, 0, 4]])

# Verificar linealmente independientes y mostrar resultados
print("Resultados:")
print("------------------------------")
soluciones_a, independiente_a = verificar_linealmente_independientes(conjunto_a)
mostrar_resultados_letra("a", conjunto_a, soluciones_a, independiente_a)

soluciones_b, independiente_b = verificar_linealmente_independientes(conjunto_b)
mostrar_resultados_letra("b", conjunto_b, soluciones_b, independiente_b)

soluciones_c, independiente_c = verificar_linealmente_independientes(conjunto_c)
mostrar_resultados_letra("c", conjunto_c, soluciones_c, independiente_c)
print("------------------------------")
