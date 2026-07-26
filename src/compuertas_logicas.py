def evaluar_expresion_1(A, B, C):
    parte1 = False
    if A:
        if B:
            parte1 = True
        else:
            parte1 = False
    else:
        parte1 = False
        
    parte2 = False
    if C:
        parte2 = False
    else:
        parte2 = True
        
    if parte1:
        return True
    else:
        if parte2:
            return True
        else:
            return False

def evaluar_expresion_2(A, B, C):
    parte1 = False
    if A:
        if B:
            parte1 = False
        else:
            parte1 = True
    else:
        if B:
            parte1 = True
        else:
            parte1 = False
            
    if parte1:
        if C:
            return True
        else:
            return False
    else:
        return False

def evaluar_expresion_3(A, B, C):
    parte1 = False
    if A:
        parte1 = True
    else:
        if B:
            parte1 = True
        else:
            parte1 = False
            
    not_A = False
    if A:
        not_A = False
    else:
        not_A = True
        
    parte2 = False
    if not_A:
        parte2 = True
    else:
        if C:
            parte2 = True
        else:
            parte2 = False
            
    if parte1:
        if parte2:
            return True
        else:
            return False
    else:
        return False


def generar_tabla_completa():
    valores = [True, False]
    
    print("=== TABLAS DE VERDAD INTEGRADAS ===")
    print("E1 = (A AND B) OR (NOT C)")
    print("E2 = (A XOR B) AND C")
    print("E3 = (A OR B) AND (NOT A OR C)\n")
    
    print(f"{'A':<7} | {'B':<7} | {'C':<7} | {'E1':<7} | {'E2':<7} | {'E3':<7}")
    print("-" * 55)
    
    for A in valores:
        for B in valores:
            for C in valores:
                res1 = evaluar_expresion_1(A, B, C)
                res2 = evaluar_expresion_2(A, B, C)
                res3 = evaluar_expresion_3(A, B, C)
                
                print(f"{str(A):<7} | {str(B):<7} | {str(C):<7} | {str(res1):<7} | {str(res2):<7} | {str(res3):<7}")

if __name__ == "__main__":
    generar_tabla_completa()