<h1 align=center>Práctica de katas de programación</h1>

Debes de crear la función `process_matrix`.

## Función `process_matrix`

Recibe como parámetro una matriz (lista de listas) de números y devuelve otra, con el mismo tamaño y número de elementos.

`process_matrix` transforma los elementos de la matriz original.

### Transformación

<hr>

La transformación que aplica es la siguiente: <b>cada elemento de la matriz pasa a tener como valor el promedio de su valor antiguo y los valores de sus vecinos</b>.

#### <b>Vecinos</b>

Se considera vecino aquel elemento con el se comparte una arista.

<img src="https://github.com/claraMirandaZ/keepcoding-practica-katas-programacion/blob/main/images/vecinos.PNG" alt="vecinos">

#### <em>Tipos de elementos</em>

- Los elementos que están en el interior tienen <b>4 vecinos</b>. Son el caso general.
- Los elementos que se encuentran en el borde tienen <b>3 vecinos</b>. Son una excepción.
- Los elementos que se encuentran en las esquinas tienen <b>2 vecinos</b>. Son otra excepción.

### Promedio

<hr>

#### <em>Antes</em>

<img src="https://github.com/claraMirandaZ/keepcoding-practica-katas-programacion/blob/main/images/antes.PNG" alt="antes">

#### <em>Después</em>

<img src="https://github.com/claraMirandaZ/keepcoding-practica-katas-programacion/blob/main/images/despues.PNG" alt="despues">

Esto mismo se debe de aplicar a todos y cada uno de los elementos de la matriz.

### Proceso de solución

<hr>

Está claro que deberemos iterar por todos los elementos de la matriz (lista de listas).

#### <b>Índices</b>

Para acceder a cada elemento, usaremos dos índices (`i` y `j`), siendo que `i` representa la columna y `j` la fila.

<img src="https://github.com/claraMirandaZ/keepcoding-practica-katas-programacion/blob/main/images/indices.PNG" alt="indices">

Para recorrer todos los elementos vamos a necesitar un bucle anidado (un `for` dentro de otro):

```
for i, column in enumerate(matrix):
    for j, value in enumerate(column):
new_value = process_element(...)
```

#### `process_element`

Vista la estructura general, procesar una lista y devolver otra, cosa que ya hemos visto mil veces, podemos centrarnos en la transformación que vamos a aplicar a cada uno de los elementos.

La función `process_element` va a recibir los índices del elemento y la matriz original, y devolverá el nuevo valor.

### Divide y vencerás

<hr>

A primera vista, la tarea se puede descomponer en las siguientes subtareas:

1. Descubrir los vecinos de un elemento.
2. Obtener su promedio.
3. Promediarlo con el valor antiguo.

El principal escollo parece ser el hecho de que según cual sea el elemento, el número de vecinos cambia. Da la impresión de que tendremos tres reglas de vecindario: <b>interior</b>, <b>borde</b> y <b>esquina</b>.

#### <b>Versión reducida</b>

Para poder empezar, vamos a resolver una versión reducida del problema, antes de ponernos con la versión completa. En vez de una matriz, vamos a procesar una lista.

La función `process_list` hace lo mismo que la función `process_matrix`, pero actúa sobre una única lista de números.

Esto simplifica el bucle principal y, sobre todo, simplifica la tarea de encontrar vecinos. Ahora solo hay dos tipos (en vez de tres):

- <b>Interior</b>: tiene dos vecinos.
- <b>Borde</b>: el primero y el último sólo tienen un vecino.

Una vez tengas resuelta la versión reducida, puedes ya abordar la versión completa.

Haremos hasta aquí juntos.

### ¿Qué hemos creado?

<hr>

El proceso de transformar cada punto en el promedio de sus vecinos es un filtro de imágenes muy común. La gran diferencia está en el tamaño de las imágenes, representadas como matrices de píxeles (tres números que representan los componentes rojo, verde y azul), son mucho mayores que las que hemos visto aquí.

Al ir promediando los valores, lo que hacemos es eliminar detalles y bordes, es decir, difuminamos la imágen. Has creado un filtro para eliminar poros abiertos, arrugas y patas de gallo en Instagram :P

Si en vez de procesar cada elemento lo hubiésemos hecho por bloques, en vez de suavizar, estaríamos pixelando la imagen. Si, además, solo lo aplicas a un rango de índices (en vez de toda la matriz), habríamos pixelado una parte de la imagen.
