def dijkstra(grafo, inicio, destino):
    if inicio not in grafo or destino not in grafo:
        return float('inf'), []

    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    rutas = {nodo: [] for nodo in grafo}
    rutas[inicio] = [inicio]
    
    nodos_no_visitados = list(grafo.keys())
    
    while nodos_no_visitados:
        nodo_actual = None
        distancia_minima = float('inf')
        
        for nodo in nodos_no_visitados:
            if distancias[nodo] < distancia_minima:
                distancia_minima = distancias[nodo]
                nodo_actual = nodo
                
        if nodo_actual is None or nodo_actual == destino:
            break
            
        nodos_no_visitados.remove(nodo_actual)
        
        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancias[nodo_actual] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                rutas[vecino] = rutas[nodo_actual] + [vecino]
                
    return distancias[destino], rutas[destino]

def cerrar_estacion(grafo, estacion_cerrada):
    nuevo_grafo = {}
    for nodo, conexiones in grafo.items():
        if nodo != estacion_cerrada:
            nuevas_conexiones = {}
            for vecino, peso in conexiones.items():
                if vecino != estacion_cerrada:
                    nuevas_conexiones[vecino] = peso
            nuevo_grafo[nodo] = nuevas_conexiones
    return nuevo_grafo

def evaluar_impacto(distancia_antes, distancia_despues):
    if distancia_antes == float('inf'):
        return "N/A", "Ya estaba desconectado"
    else:
        if distancia_despues == float('inf'):
            return "N/A", "Desconectado"
        else:
            diferencia = distancia_despues - distancia_antes
            if diferencia == 0:
                return str(diferencia), "Sin impacto"
            else:
                return str(diferencia), "Ruta más larga"

if __name__ == "__main__":
    ciudad = {
        'Portal': {'Calle26': 5, 'Estadio': 8},
        'Calle26': {'Portal': 5, 'Centro': 6, 'Parque': 4},
        'Estadio': {'Portal': 8, 'Parque': 7, 'Museo': 10},
        'Centro': {'Calle26': 6, 'Museo': 3, 'Universidad': 5},
        'Parque': {'Calle26': 4, 'Estadio': 7, 'Universidad': 4, 'Biblioteca': 6},
        'Museo': {'Estadio': 10, 'Centro': 3, 'Biblioteca': 8},
        'Universidad': {'Centro': 5, 'Parque': 4, 'Biblioteca': 2},
        'Biblioteca': {'Parque': 6, 'Museo': 8, 'Universidad': 2}
    }
    rutas_prueba = [
        ('Portal', 'Universidad'),
        ('Estadio', 'Biblioteca'),
        ('Calle26', 'Museo'),
        ('Portal', 'Centro'), 
        ('Parque', 'Museo')
    ]
    
    estacion_a_cerrar = 'Centro'
    ciudad_cerrada = cerrar_estacion(ciudad, estacion_a_cerrar)
    
    print("\nSimulando el cierre de la estación: " + estacion_a_cerrar + "\n")
    print(f"{'Origen':<12} | {'Destino':<12} | {'Dist. Antes':<11} | {'Dist. Después':<13} | {'Diferencia':<10} | {'Estado'}")
    print("-" * 85)
    
    for origen, destino in rutas_prueba:
        dist_antes, ruta_a = dijkstra(ciudad, origen, destino)
        dist_despues, ruta_d = dijkstra(ciudad_cerrada, origen, destino)
        
        str_antes = str(dist_antes) if dist_antes != float('inf') else "Inf"
        str_despues = str(dist_despues) if dist_despues != float('inf') else "Inf"
        
        diferencia, estado = evaluar_impacto(dist_antes, dist_despues)
        
        print(f"{origen:<12} | {destino:<12} | {str_antes:<11} | {str_despues:<13} | {diferencia:<10} | {estado}")