def colorear_grafo(grafo):
    colores_asignados = {}
    
    for materia in grafo:
        colores_vecinos = []
        for vecino in grafo[materia]:
            if vecino in colores_asignados:
                colores_vecinos.append(colores_asignados[vecino])
                
        color_prueba = 1
        color_encontrado = False
        
        while not color_encontrado:
            if color_prueba not in colores_vecinos:
                color_encontrado = True
            else:
                color_prueba += 1
                
        colores_asignados[materia] = color_prueba
        
    return colores_asignados

def verificar_coloreo(grafo, colores_asignados):
    es_valido = True
    for materia in grafo:
        color_actual = colores_asignados[materia]
        for vecino in grafo[materia]:
            if colores_asignados[vecino] == color_actual:
                es_valido = False
    return es_valido
if __name__ == "__main__":
    
    grafo_materias = {
        'Matematicas': ['Fisica', 'Programacion', 'Logica'],
        'Fisica': ['Matematicas', 'Quimica', 'Estadistica'],
        'Quimica': ['Fisica', 'Biologia'],
        'Programacion': ['Matematicas', 'BasesDatos', 'Redes'],
        'BasesDatos': ['Programacion', 'Redes'],
        'Redes': ['Programacion', 'BasesDatos', 'Ingles'],
        'Ingles': ['Redes', 'Etica'],
        'Etica': ['Ingles', 'Logica'],
        'Logica': ['Matematicas', 'Etica', 'Estadistica'],
        'Estadistica': ['Fisica', 'Logica', 'Biologia'],
        'Biologia': ['Quimica', 'Estadistica']
    }

    grafo_generico = {
        'V1': ['V2', 'V3', 'V4'],
        'V2': ['V1', 'V5', 'V6'],
        'V3': ['V1', 'V7'],
        'V4': ['V1', 'V8', 'V9', 'V10'],
        'V5': ['V2', 'V10'],
        'V6': ['V2', 'V7'],
        'V7': ['V3', 'V6', 'V8'],
        'V8': ['V4', 'V7', 'V9'],
        'V9': ['V4', 'V8'],
        'V10': ['V4', 'V5']
    }

    pruebas = [
        ("Prueba 1: Horarios de Materias", grafo_materias),
        ("Prueba 2: Grafo Genérico de 10 Nodos", grafo_generico)
    ]

    for nombre_prueba, grafo_actual in pruebas:
        print("=== " + nombre_prueba + " ===")
        
        resultado_colores = colorear_grafo(grafo_actual)
        
        if verificar_coloreo(grafo_actual, resultado_colores):
            print("Verificación: ¡EXITOSA! Coloreo válido.")
        else:
            print("Verificación: ERROR. Nodos adyacentes comparten color.")

        grupos = {}
        for nodo, color in resultado_colores.items():
            if color not in grupos:
                grupos[color] = []
            grupos[color].append(nodo)
            
        print("Total de colores (franjas) usados: " + str(len(grupos)))
        
        for color, nodos in grupos.items():
            print("Color " + str(color) + ": " + ", ".join(nodos))
            
        print("\n" + "="*50 + "\n")