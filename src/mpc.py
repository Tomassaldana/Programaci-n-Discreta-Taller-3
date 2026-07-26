import random

def dividir_nota(nota, M):
    s1 = random.randint(0, M - 1)
    s2 = random.randint(0, M - 1)
    
    s3 = (nota - s1 - s2) % M
    
    return s1, s2, s3

def simulacion_mpc(notas, M):
    suma_servidor_1 = 0
    suma_servidor_2 = 0
    suma_servidor_3 = 0
    
    print("\n--- Repartiendo fragmentos a los servidores ---")
    
    for nota in notas:
        s1, s2, s3 = dividir_nota(nota, M)
        
        suma_servidor_1 = (suma_servidor_1 + s1) % M
        suma_servidor_2 = (suma_servidor_2 + s2) % M
        suma_servidor_3 = (suma_servidor_3 + s3) % M
        
    print("Servidor 1 reporta su suma parcial: " + str(suma_servidor_1))
    print("Servidor 2 reporta su suma parcial: " + str(suma_servidor_2))
    print("Servidor 3 reporta su suma parcial: " + str(suma_servidor_3))
    
    print("\n--- Reconstruyendo resultado final ---")
    suma_total = (suma_servidor_1 + suma_servidor_2 + suma_servidor_3) % M
    promedio = suma_total / len(notas)
    
    return suma_total, promedio

if __name__ == "__main__":
    M = 1000003
    
    print("=== PRUEBA OBLIGATORIA DEL TALLER ===")
    notas_prueba = [40, 35, 50, 25]
    print("Notas originales (ocultas a los servidores): " + str(notas_prueba))
    
    suma_total, promedio = simulacion_mpc(notas_prueba, M)
    
    print("-> Suma total calculada: " + str(suma_total))
    print("-> Promedio calculado: " + str(promedio))

    print("\n=== PROBAR CON NUEVAS NOTAS ===")
    entrada = input("Ingresa notas separadas por espacio (ej: 10 20 30): ")
    
    lista_cadenas = entrada.split()
    notas_usuario = []
    datos_validos = True
    
    if len(lista_cadenas) == 0:
        datos_validos = False
    else:
        for cadena in lista_cadenas:
            if cadena.isdigit():
                nota_int = int(cadena)
                if nota_int >= 0:
                    if nota_int <= 50:
                        notas_usuario.append(nota_int)
                    else:
                        datos_validos = False
                else:
                    datos_validos = False
            else:
                datos_validos = False

    if datos_validos:
        suma_usr, prom_usr = simulacion_mpc(notas_usuario, M)
        print("\n-> Suma total calculada: " + str(suma_usr))
        print("-> Promedio calculado: " + str(prom_usr))
    else:
        print("Error: Debes ingresar únicamente números enteros entre 0 y 50 separados por espacios.")