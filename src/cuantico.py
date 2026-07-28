import math
import random

# operaciones de Vectores y Matrices

def multiplicar_matriz_vector(matriz, vector):
    nuevo_alpha = matriz[0][0] * vector[0] + matriz[0][1] * vector[1]
    nuevo_beta  = matriz[1][0] * vector[0] + matriz[1][1] * vector[1]
    return [nuevo_alpha, nuevo_beta]

# compuertas Cuánticas

def compuerta_X(vector):
    """Compuerta NOT cuántica (Invierte 0 y 1)."""
    matriz_X = [[0, 1], 
                [1, 0]]
    return multiplicar_matriz_vector(matriz_X, vector)

def compuerta_Z(vector):
    """Compuerta de fase Z."""
    matriz_Z = [[1,  0], 
                [0, -1]]
    return multiplicar_matriz_vector(matriz_Z, vector)

def compuerta_H(vector):
    raiz2 = math.sqrt(2)
    matriz_H = [[1/raiz2,  1/raiz2], 
                [1/raiz2, -1/raiz2]]
    return multiplicar_matriz_vector(matriz_H, vector)

# probabilidades y Medición

def calcular_probabilidades(vector):
    """Calcula las probabilidades teóricas: |alpha|^2 y |beta|^2."""
    prob_0 = (vector[0] * vector[0])
    prob_1 = (vector[1] * vector[1])
    return prob_0, prob_1

def simular_mediciones(vector, num_mediciones=1000):
    prob_0, prob_1 = calcular_probabilidades(vector)
    
    cuenta_0 = 0
    cuenta_1 = 0
    
    for _ in range(num_mediciones):
        tiro = random.random() # Genera número entre 0 y 1
        
        if tiro < prob_0:
            cuenta_0 = cuenta_0 + 1
        else:
            cuenta_1 = cuenta_1 + 1
            
    return cuenta_0, cuenta_1

def imprimir_resultados(nombre_prueba, vector_resultado):
    print(f"=== {nombre_prueba} ===")
    print(f"Estado del qubit: [{vector_resultado[0]:.4f}, {vector_resultado[1]:.4f}]")
    
    prob_0, prob_1 = calcular_probabilidades(vector_resultado)
    print(f"Probabilidades teóricas: P(0) = {prob_0*100:.1f}%, P(1) = {prob_1*100:.1f}%")
    
    c_0, c_1 = simular_mediciones(vector_resultado, 1000)
    print("Resultados de 1000 mediciones:")
    print(f" -> Ceros observados: {c_0}")
    print(f" -> Unos observados:  {c_1}\n")

# pruebas
if __name__ == "__main__":
    estado_cero = [1.0, 0.0]
    
    res_prueba1 = compuerta_X(estado_cero)
    imprimir_resultados("Prueba 1: Compuerta X sobre |0> (Esperado: |1>)", res_prueba1)
    
    res_prueba2 = compuerta_H(estado_cero)
    imprimir_resultados("Prueba 2: Compuerta H sobre |0> (Esperado: 50% y 50%)", res_prueba2)
    
    res_temporal = compuerta_H(estado_cero)
    res_prueba3 = compuerta_H(res_temporal)
    imprimir_resultados("Prueba 3: Compuerta H doble sobre |0> (Esperado: Vuelve a |0>)", res_prueba3)