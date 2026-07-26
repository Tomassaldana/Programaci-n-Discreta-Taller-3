def dijkstra(grafo, inicio, destino):
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


# Grafo de la Ciudad (8 Vértices, 12 Aristas)

# Las 12 conexiones (aristas) son:
# 1. Portal-Calle26 (5)    2. Portal-Estadio (8)    3. Calle26-Centro (6) 
# 4. Calle26-Parque (4)    5. Estadio-Parque (7)    6. Estadio-Museo (10)
# 7. Centro-Museo (3)      8. Centro-Universidad(5) 9. Parque-Universidad(4)
# 10. Parque-Biblioteca(6) 11. Museo-Biblioteca(8)  12. Universidad-Biblioteca(2)

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

if __name__ == "__main__":
    print("=== ESTACIONES DISPONIBLES ===")
    for estacion in ciudad.keys():
        print("- " + estacion)
        
    print("\n--- PRUEBA OBLIGATORIA DEL TALLER ---")
    inicio_prueba = 'Portal'
    destino_prueba = 'Universidad'
    distancia, ruta = dijkstra(ciudad, inicio_prueba, destino_prueba)
    
    print("Ruta más corta desde " + inicio_prueba + " hasta " + destino_prueba + ":")
    print("Recorrido: " + str(ruta))
    print("Distancia total: " + str(distancia))
    print("\n=== BUSCAR UNA NUEVA RUTA ===")
    origen = input("Ingresa la estación de origen (tal cual está escrita arriba): ")
    
    if origen in ciudad:
        destino = input("Ingresa la estación de destino: ")
        if destino in ciudad:
            if origen == destino:
                print("Ya estás en tu destino. Distancia: 0")
            else:
                dist_usr, ruta_usr = dijkstra(ciudad, origen, destino)
                print("\n-> Resultados:")
                print("Recorrido exacto: " + " -> ".join(ruta_usr))
                print("Distancia / Tiempo total: " + str(dist_usr))
        else:
            print("Error: La estación de destino no existe en el mapa.")
    else:
        print("Error: La estación de origen no existe en el mapa.")