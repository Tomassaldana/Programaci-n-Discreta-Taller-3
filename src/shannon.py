import math

def analizar_texto(texto):

    if len(texto) == 0:
        return 0.0
        
    frecuencias = {}
    for simbolo in texto:
        if simbolo in frecuencias:
            frecuencias[simbolo] = frecuencias[simbolo] + 1
        else:
            frecuencias[simbolo] = 1
            
    longitud_total = len(texto)
    entropia_total = 0.0
    
    print("Símbolo | Frecuencia | Probabilidad")
    print("-" * 37)
    
    for simbolo, frec in frecuencias.items():
        probabilidad = frec / longitud_total
        
        entropia_parcial = probabilidad * math.log2(probabilidad)
        entropia_total = entropia_total - entropia_parcial
        
        simbolo_impreso = simbolo
        if simbolo == " ":
            simbolo_impreso = "[espacio]"
            
        print(f"{simbolo_impreso:<7} | {frec:<10} | {probabilidad:.4f}")
        
    return entropia_total

if __name__ == "__main__":
    
    texto_repetitivo = "AAAAAAAAAABBBBBBBBBB"
    texto_variado = "MURCIELAGO VOLADOR"
    
    print("=== ANÁLISIS DE ENTROPÍA DE SHANNON ===")
    
    print(f"\nTexto 1 (Repetitivo): '{texto_repetitivo}'")
    entropia_rep = analizar_texto(texto_repetitivo)
    print(f"-> ENTROPÍA TEXTO 1: {entropia_rep:.4f} bits por símbolo")
    
    print("=" * 45)
    
    print(f"\nTexto 2 (Variado): '{texto_variado}'")
    entropia_var = analizar_texto(texto_variado)
    print(f"-> ENTROPÍA TEXTO 2: {entropia_var:.4f} bits por símbolo")
    
    print("=" * 45)
    
    print("\n=== CONCLUSIÓN DE LA COMPARACIÓN ===")
    if entropia_rep > entropia_var:
        print("El Texto 1 tiene mayor entropía.")
    else:
        if entropia_var > entropia_rep:
            print("El Texto 2 tiene mayor entropía.")
        else:
            print("Ambos textos tienen exactamente la misma entropía.")