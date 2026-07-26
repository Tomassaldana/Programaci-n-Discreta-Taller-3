def cifrar_cesar(texto, k):
    alfabeto_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minus = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    for caracter in texto:
        if caracter in alfabeto_mayus:
            indice = (alfabeto_mayus.index(caracter) + k) % 26
            resultado += alfabeto_mayus[indice]
        else:
            if caracter in alfabeto_minus:
                indice = (alfabeto_minus.index(caracter) + k) % 26
                resultado += alfabeto_minus[indice]
            else:
                resultado += caracter
                
    return resultado

def descifrar_cesar(texto_cifrado, k):
    return cifrar_cesar(texto_cifrado, -k)

def fuerza_bruta_cesar(texto_cifrado):
    print("\n--- Iniciando ataque de fuerza bruta ---")
    for k in range(1, 26):
        intento = descifrar_cesar(texto_cifrado, k)
        print("Intento con k=" + str(k) + ": " + intento)

if __name__ == "__main__":
    corriendo = True
    while corriendo:
        print("\n=== MENÚ: CIFRADO CÉSAR ===")
        print("1. Cifrar un mensaje")
        print("2. Descifrar un mensaje")
        print("3. Romper mensaje (Fuerza bruta)")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            mensaje = input("Ingresa el mensaje a cifrar: ")
            k_str = input("Ingresa el desplazamiento (número entero k): ")
            
            es_numero = False
            if k_str.isdigit():
                es_numero = True
            else:
                if k_str.startswith("-"):
                    if k_str[1:].isdigit():
                        es_numero = True
            
            if es_numero:
                k = int(k_str)
                cifrado = cifrar_cesar(mensaje, k)
                print("\n-> Resultado cifrado: " + cifrado)
            else:
                print("Error: El desplazamiento debe ser un número entero.")
                
        else:
            if opcion == '2':
                mensaje = input("Ingresa el mensaje a descifrar: ")
                k_str = input("Ingresa el desplazamiento (número entero k): ")
                
                es_numero = False
                if k_str.isdigit():
                    es_numero = True
                else:
                    if k_str.startswith("-"):
                        if k_str[1:].isdigit():
                            es_numero = True
                
                if es_numero:
                    k = int(k_str)
                    descifrado = descifrar_cesar(mensaje, k)
                    print("\n-> Resultado descifrado: " + descifrado)
                else:
                    print("Error: El desplazamiento debe ser un número entero.")
                    
            else:
                if opcion == '3':
                    mensaje = input("Ingresa el mensaje cifrado a romper: ")
                    fuerza_bruta_cesar(mensaje)
                else:
                    if opcion == '4':
                        print("Saliendo del programa...")
                        corriendo = False
                    else:
                        print("Opción no válida. Intenta de nuevo.")