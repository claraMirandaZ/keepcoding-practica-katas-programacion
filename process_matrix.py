from functools import reduce

def process_matrix(matrix):
    '''
    Recibe una matriz (lista de listas) de números y devuelve una nueva (con el mismo tamaño y número de elementos) con sus elementos cambiados. Cada elemento de la nueva matriz será el promedio del valor antiguo y el de sus vecinos.
    Con process_matrix transformamos los elementos de la matriz original.
    '''

    # Matriz vacía que ir rellenando
    processed_matrix = []

    # Matriz con un único array (una sola "columna")
    if len(matrix) == 1:
        for j, column in enumerate(matrix[0]):
            new_element = process_element(0, j, matrix)
            processed_matrix.append(new_element)
    # Matriz con más de una columna
    else:
        for i, row in enumerate(matrix):
            row = []
            for j, column in enumerate(matrix[0]):
                new_element = process_element(i, j, matrix)
                row.append(new_element)
            processed_matrix.append(row)

    return processed_matrix

def process_element(i, j, matrix):
    '''
    Recibe la posición (dos coordenadas) de un elemento y calculamos su promedio con sus vecinos (y lo devuelve)
    '''

    # Obtención de la lista de las posiciones del elemento y sus vecinos
    positions_list = get_neighbour_position(i, j, matrix)
    # Obtención de la lista de los valores de los vecinos que existen dentro de la matriz
    values_list = get_neighbour_values(positions_list, matrix)
    # Cálculo del promedio
    avrg = get_average(values_list)
    # Devolución del valor final
    return avrg

def get_neighbour_position(i, j, matrix):
    '''
    Devuelve la lista de las posiciones del elemento y sus vecinos
    '''

    positions_list = []
    # Sólo un array (una sola "columna")
    if len(matrix) == 1:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i, j+1])
    # Una matriz propiamente dicha (varias columnas)
    else:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i-1, j])
        positions_list.append([i, j+1])
        positions_list.append([i+1, j])
    return positions_list

def get_neighbour_values(positions_list, matrix):
    '''
    Valorando los cinco posibles vecinos, devuelve una lista con los valores del elemento y sus vecinos QUE SÍ EXISTEN (desestima, en bordes y esquinas, los vecinos que no existen)
    '''

    values = []
    for i in range(len(positions_list)):
        # Si la posición del vecino es menor que cero y mayor que la longitud de la matriz (aka "fuera de la matriz"), basándome en sus coordenadas en positions_list ([i][0] y [i][1]) (no existen)
        if (positions_list[i][0] >= 0 and positions_list[i][0] < (len(matrix))) and (positions_list[i][1] >= 0 and positions_list[i][1] < (len(matrix[0]))):
            # Sacamos el valor del elemento y vecinos dentro de la matriz (existen)
            elt_value = matrix[positions_list[i][0]][positions_list[i][1]]
            # Añadimos cada uno de esos valores al array values (inicialmente vacío)
            values.append(elt_value)
    return values

def get_average(numbers):
    '''
    Recibe una lista de números y devuelve su promedio
    '''
    return reduce(lambda accum, x: accum + x, numbers, 0) / len(numbers)