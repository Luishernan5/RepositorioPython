import numpy as np

def print_matrix(matrix, name):
    print(f"{name} =")
    print(np.array_str(matrix, precision=3, suppress_small=True))
    print()

def can_be_expressed_as_linear_combination(S, v):
    # Convert S to a matrix and v to a vector
    A = np.array(S).T
    b = np.array(v).reshape(-1, 1)
    
    # Create the augmented matrix
    augmented_matrix = np.hstack((A, b))
    
    print_matrix(A, "Matriz inicial A")
    print_matrix(augmented_matrix, "Matriz aumentada [A|b]")
    
    # Perform Gaussian elimination
    try:
        # Use np.linalg.lstsq to solve the system (for the sake of simplicity)
        solution, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        augmented_matrix_final = np.hstack((A, b - np.dot(A, solution)))
        
        print_matrix(augmented_matrix_final, "Matriz final [A|b'] (con resultados de mínimos cuadrados)")

        if np.allclose(A @ solution, b):
            return True, solution
        else:
            return False, None
    except np.linalg.LinAlgError:
        return False, None

# Define the space S
S = [(6, -7, 8, 6), (4, 6, -4, 1)]

# Define the vectors to check
u = (-42, 113, -112, -60)
v = (24.5, 24.5, -14, 9.5)  # Simplified 49/2 to 24.5, 98/4 to 24.5, 19/2 to 9.5
w = (-4, -14, 13.5, 6.625)  # Simplified 27/2 to 13.5, 53/8 to 6.625
z = (8, 4, -1, 4.25)       # Simplified 17/4 to 4.25

# List of vectors to verify
vectors = [u, v, w, z]
vector_names = ['u', 'v', 'w', 'z']

# Check each vector
for i, vec in enumerate(vectors):
    print(f"Chequeando el vector {vector_names[i]} = {vec}")
    result, coefficients = can_be_expressed_as_linear_combination(S, vec)
    if result:
        print(f"El vector {vector_names[i]} se puede expresar como una combinación lineal de los vectores de S con coeficientes: {coefficients.ravel()}")
    else:
        print(f"El vector {vector_names[i]} NO se puede expresar como una combinación lineal de los vectores de S.")
    print("\n" + "-"*50 + "\n")