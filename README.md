# PilotoTutoria
Implementación del modelo de segmentación de estudiantes 

## Modelo

+ Genera un modelo de segmenctación usando K-Means usando reducción de dimensionalidad con análisis de componentes principales (PCA)
+ Se obtiene el número de clusters usando la curva de elbow y el método de la silueta 
+ Se normaliza usando StandardScaler

## Generación de datos

+ Se implementa una rutina para generar datos aleatorios para generar la primera aproximación del modelo

## Consideraciones
1. Se debe trabajar con un **archivo CSV** que contenga los resultados de la evaluación considerando los puntajes, de acuerdo a escala de valoración

2. La **cantidad de ítems**, dependerá de el detalle de la rúbrica asociada a la evaluación y debe ser definido.

3. La escala es la estándar que se maneja:

  + ED - Logro del aspecto en un 100%
  + AD - Logro del aspecto entre un 80% y un 99%
  + DA - Logro del aspecto entre un 60% y un 79%
  + DP - Logro del aspecto entre un 30% y un 59%
  + DC - Logro del aspecto inferior al 30%
  
  Cada uno de estos valores se escala de 1 a 5 

4. El archivo CSV de contar con las columnas OBLIGATORIAS:

  + ID del estudiante 
  + $I_{i}$ considerando cada ítem evaluado 

5. Considerando el archivo CSV se calculan 2 columnas: ***nota y categoría***.

6. Cálculo de la nota (en base al puntaje)
7. Cálculo de la **categoría** en base a la nota
8. Los candidatos a tutoría serán aquellos que estén en la **categoría 4 o 5**
