# Desarrollo del tercer taller del curso de matematicas discretas

¡Hola! Bienvenido a este repositorio. Aquí encontrarás una colección de scripts en Python que llevan conceptos matemáticos abstractos a la práctica. Desde fundamentos de criptografía y teoría de grafos, hasta lógica booleana y simulación cuántica.

Este proyecto fue construido como un laboratorio educativo para explorar y demostrar cómo las matemáticas sustentan las tecnologías complejas que usamos todos los días.

---

## 📂 Contenido del Repositorio

El proyecto está dividido en varios módulos independientes, cada uno enfocado en resolver un problema específico:

* **Ejercicio 2: RSA de Juguete**
  Simulador del famoso algoritmo de seguridad RSA a pequeña escala. Demuestra el uso de la aritmética modular y el algoritmo de Euclides para la generación de llaves criptográficas.
* **Ejercicio 3: Computación Multipartita Segura (MPC)**
  Sistema para calcular el promedio de un grupo de notas dividiendo la información. Logra el resultado correcto ocultando los datos originales mediante la "partición de secretos".
* **Ejercicio 4: Ruta Más Corta (Dijkstra)**
  Un mini "Google Maps" basado en grafos. Utiliza el algoritmo de Dijkstra para calcular la ruta más rápida y óptima entre dos estaciones de transporte.
* **Ejercicio 5: Análisis de Impacto en Redes**
  Extensión del ejercicio de rutas. Simula matemáticamente el cierre de una estación clave del sistema, extirpando un vértice del grafo para medir el impacto y los nuevos cuellos de botella.
* **Ejercicio 6: Coloreo de Grafos**
  Algoritmo voraz (*Greedy*) diseñado para armar horarios universitarios. Asigna colores a los vértices (materias) para garantizar que no existan cruces, simulando franjas horarias.
* **Ejercicio 7: Tablas de Verdad**
  Generador automático de lógica proposicional. Evalúa múltiples expresiones booleanas simultáneas para tres variables y dibuja la tabla de verdad completa en consola.
* **Ejercicio 8: Simplificación Booleana**
  Optimizador lógico. Toma una expresión compleja de mintérminos y la reduce a su forma más sencilla mediante agrupación y eliminación de redundancias, comprobando la equivalencia final.
* **Ejercicio 9: Entropía de Shannon**
  Programa basado en la Teoría de la Información. Analiza cadenas de texto y calcula la incertidumbre (en bits por símbolo) de acuerdo a las frecuencias y probabilidades de aparición de sus caracteres.
* **Ejercicio 10: Simulador Cuántico (Qubits)**
  Modelo impulsado por álgebra lineal que simula el comportamiento de un *qubit*. Aplica compuertas (X, Z, H) utilizando matrices $2 \times 2$ y simula mediciones para observar el colapso del estado cuántico.

---

## 🚀 Instalación y Ejecución

Todos los ejercicios fueron diseñados para ser ligeros y correr en cualquier entorno sin dolores de cabeza.

1. **Requisitos:** Solo necesitas tener instalado **Python 3.x**. El código se apoya puramente en la lógica nativa del lenguaje y utiliza únicamente librerías estándar (como `math` y `random`). Cero instalaciones externas.
2. **Clonar y probar:** Descarga este repositorio, abre tu terminal favorita y ejecuta cualquiera de los archivos. Por ejemplo:
   ```bash
   python ejercicio_4_dijkstra.py
