def convertir_a_binario_3bits(n):
    res = ""
    if n >= 4:
        res = res + "1"
        n = n - 4
    else:
        res = res + "0"
        
    if n >= 2:
        res = res + "1"
        n = n - 2
    else:
        res = res + "0"
        
    if n >= 1:
        res = res + "1"
    else:
        res = res + "0"
        
    return res

def formatear_termino(t):
    variables = []
    
    if t[0] == '1':
        variables.append("A")
    else:
        if t[0] == '0':
            variables.append("(NOT A)")
            
    if t[1] == '1':
        variables.append("B")
    else:
        if t[1] == '0':
            variables.append("(NOT B)")
            
    if t[2] == '1':
        variables.append("C")
    else:
        if t[2] == '0':
            variables.append("(NOT C)")
            
    if len(variables) == 0:
        return "1"
    else:
        return " AND ".join(variables)

def generar_expresion_original(minterminos):
    lista_terminos = []
    for m in minterminos:
        binario = convertir_a_binario_3bits(m)
        termino_legible = formatear_termino(binario)
        lista_terminos.append("(" + termino_legible + ")")
    
    return " OR ".join(lista_terminos)

def combinar_terminos(terminos):
    nuevos_terminos = []
    marcados = [False] * len(terminos)
    
    for i in range(len(terminos)):
        for j in range(i + 1, len(terminos)):
            diferencias = 0
            str_combinado = ""
            
            for k in range(3):
                if terminos[i][k] != terminos[j][k]:
                    diferencias = diferencias + 1
                    str_combinado = str_combinado + "-"
                else:
                    str_combinado = str_combinado + terminos[i][k]
                    
            if diferencias == 1:
                if str_combinado not in nuevos_terminos:
                    nuevos_terminos.append(str_combinado)
                marcados[i] = True
                marcados[j] = True
                
    terminos_finales = []
    
    for i in range(len(terminos)):
        if not marcados[i]:
            if terminos[i] not in terminos_finales:
                terminos_finales.append(terminos[i])
                
    for t in nuevos_terminos:
        if t not in terminos_finales:
            terminos_finales.append(t)
            
    hubo_cambio = False
    if len(nuevos_terminos) > 0:
        hubo_cambio = True
        
    return terminos_finales, hubo_cambio

def simplificar_minterminos(minterminos):
    terminos = []
    for m in minterminos:
        terminos.append(convertir_a_binario_3bits(m))
        
    hubo_cambio = True
    while hubo_cambio:
        terminos, hubo_cambio = combinar_terminos(terminos)
        
    expresion_final = []
    for t in terminos:
        expresion_final.append(formatear_termino(t))
        
    return terminos, " OR ".join(expresion_final)


def evaluar_original(A, B, C, minterminos):
    val = 0
    if A: val = val + 4
    if B: val = val + 2
    if C: val = val + 1
    
    if val in minterminos:
        return True
    else:
        return False

def evaluar_simplificada(A, B, C, terminos_simp):
    for t in terminos_simp:
        coincide = True
        
        if t[0] == '1':
            if not A: coincide = False
        else:
            if t[0] == '0':
                if A: coincide = False
                
        if t[1] == '1':
            if not B: coincide = False
        else:
            if t[1] == '0':
                if B: coincide = False
                
        if t[2] == '1':
            if not C: coincide = False
        else:
            if t[2] == '0':
                if C: coincide = False
                
        if coincide:
            return True
            
    return False

if __name__ == "__main__":
    minterminos_prueba = [1, 3, 5, 7]
    
    print("=== SIMPLIFICACIÓN BOOLEANA ===")
    
    expresion_cruda = generar_expresion_original(minterminos_prueba)
    print("Función Original:")
    print(expresion_cruda + "\n")
    
    terminos_crudos, expresion_simp = simplificar_minterminos(minterminos_prueba)
    print("Función Simplificada:")
    print(expresion_simp + "\n")
    
    print("=== VERIFICACIÓN: TABLA DE VERDAD ===")
    print(f"{'A':<5} | {'B':<5} | {'C':<5} | {'Original':<10} | {'Simplificada':<12} | {'¿Coinciden?'}")
    print("-" * 65)
    
    valores = [True, False]
    verificacion_exitosa = True
    
    for A in valores:
        for B in valores:
            for C in valores:
                res_orig = evaluar_original(A, B, C, minterminos_prueba)
                res_simp = evaluar_simplificada(A, B, C, terminos_crudos)
                
                coinciden = "SÍ"
                if res_orig != res_simp:
                    coinciden = "NO"
                    verificacion_exitosa = False
                    
                print(f"{str(A):<5} | {str(B):<5} | {str(C):<5} | {str(res_orig):<10} | {str(res_simp):<12} | {coinciden}")
                
    if verificacion_exitosa:
        print("\n¡Éxito! Las tablas de verdad son idénticas. La simplificación es correcta.")
    else:
        print("\nError: Las tablas de verdad no coinciden.")