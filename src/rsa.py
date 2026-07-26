
def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x1, y1 = euclides_extendido(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return mcd, x, y

def calcular_inverso_modular(e, phi):
    mcd, x, y = euclides_extendido(e, phi)
    if mcd != 1:
        return None 
    else:
        return x % phi 

def cifrar_rsa(M, e, n):
    return pow(M, e, n)

def descifrar_rsa(C, d, n):
    return pow(C, d, n)

if __name__ == "__main__":
    print("=== PRUEBA OBLIGATORIA DEL TALLER ===")
    p = 61
    q = 53
    e = 17
    M = 65
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    print("Primos: p=" + str(p) + ", q=" + str(q))
    print("Exponente público: e=" + str(e))
    print("Mensaje original: M=" + str(M))
    print("-----------------------------------")
    
    if calcular_mcd(e, phi) != 1:
        print("Error: El exponente 'e' no es válido (gcd(e, phi) != 1).")
    else:
        d = calcular_inverso_modular(e, phi)
        C = cifrar_rsa(M, e, n)
        M_descifrado = descifrar_rsa(C, d, n)
        
        print("n = " + str(n))
        print("phi(n) = " + str(phi))
        print("Inverso modular (d) = " + str(d))
        print("Mensaje cifrado (C) = " + str(C))
        print("Mensaje descifrado = " + str(M_descifrado))
        
        if M == M_descifrado:
            print("\n¡Éxito! El mensaje descifrado coincide con el original.")
    print("\n=== PROBAR NUEVOS VALORES ===")
    entrada_p = input("Ingresa el primo p (ej. 11): ")
    entrada_q = input("Ingresa el primo q (ej. 13): ")
    entrada_e = input("Ingresa el exponente e (ej. 7): ")
    entrada_M = input("Ingresa el mensaje M (como número): ")
    
    if entrada_p.isdigit() and entrada_q.isdigit() and entrada_e.isdigit() and entrada_M.isdigit():
        p_usr = int(entrada_p)
        q_usr = int(entrada_q)
        e_usr = int(entrada_e)
        M_usr = int(entrada_M)
        
        n_usr = p_usr * q_usr
        phi_usr = (p_usr - 1) * (q_usr - 1)
        
        if calcular_mcd(e_usr, phi_usr) != 1:
            print("\nError: El valor de 'e' (" + str(e_usr) + ") no es coprimo con phi (" + str(phi_usr) + "). Intenta con otro 'e'.")
        else:
            d_usr = calcular_inverso_modular(e_usr, phi_usr)
            C_usr = cifrar_rsa(M_usr, e_usr, n_usr)
            desc_usr = descifrar_rsa(C_usr, d_usr, n_usr)
            
            print("\nResultados:")
            print("Llave pública (e, n): (" + str(e_usr) + ", " + str(n_usr) + ")")
            print("Llave privada (d, n): (" + str(d_usr) + ", " + str(n_usr) + ")")
            print("Cifrado (C): " + str(C_usr))
            print("Descifrado: " + str(desc_usr))
    else:
        print("Todos los valores deben ser números enteros positivos.")