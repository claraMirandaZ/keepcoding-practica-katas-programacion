from functools import reduce

def process_matrix(matrix):
    '''
    Recibe una matriz (lista de listas) de números y devuelve una nueva (con el mismo tamaño y número de elementos) con sus elementos cambiados. Cada elemento de la nueva matriz será el promedio del valor antiguo y el de sus vecinos.
    Con process_matrix transformamos los elementos de la matriz original.
    '''
    # Matriz vacía que ir rellenando
    processed_matrix = []

    # Matriz con una sola columna
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
    Recibe la posición (dos coordenadas) de un elemento y calcula el promedio con sus vecinos (y lo devuelve)
    '''

    # Obtención de la lista de vecinos
    positions_list = get_neighbour_position(i, j, matrix)
    values_list = get_neighbour_values(positions_list, matrix)
    # Cálculo del promedio
    avrg = get_average(values_list)
    # Devolución del valor final
    return avrg

def get_neighbour_position(i, j, matrix):
    '''
    Devuelve la lista de las posiciones de los vecinos, incluida la del propio elemento
    '''

    positions_list = []
    # Una sola columna, primer elemento
    if len(matrix) == 1 and j == 0:
        positions_list.append([i, j])
        positions_list.append([i, j+1])
    # Una sola columna, elementos centrales
    elif len(matrix) == 1 and j < len(matrix[i]) - 1:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i, j+1])
    # Una sola columna, último elemento
    elif len(matrix) == 1 and j == len(matrix[i]) - 1:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
    # Esquina superior izquierda
    elif i == 0 and j == 0:
        positions_list.append([i, j])
        positions_list.append([i+1, j])
        positions_list.append([i, j+1])
    # Esquina superior derecha
    elif i == 0 and j == len(matrix[i]) - 1:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i+1, j])
    # Esquina inferior izquierda
    elif i == len(matrix) - 1 and j == 0:
        positions_list.append([i, j])
        positions_list.append([i-1, j])
        positions_list.append([i, j+1])
    # Esquina inferior derecha
    elif i == len(matrix) - 1 and j == len(matrix[i]) - 1:
        positions_list.append([i, j])
        positions_list.append([i-1, j])
        positions_list.append([i, j-1])
    # Borde superior
    elif i == 0 and j < len(matrix[i]) - 1:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i+1, j])
        positions_list.append([i, j+1])
    # Borde lateral izquierdo
    elif i != 0 and i != len(matrix) - 1 and j == 0:
        positions_list.append([i, j])
        positions_list.append([i-1, j])
        positions_list.append([i, j+1])
        positions_list.append([i+1, j])
    # Borde lateral derecho
    elif i != 0 and i != len(matrix) - 1 and j == len(matrix[i]) - 1:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i-1, j])
        positions_list.append([i+1, j])
    # Borde inferior
    elif i == len(matrix) - 1 and j < len(matrix[i]) - 1:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i-1, j])
        positions_list.append([i, j+1])
    # Resto 
    else:
        positions_list.append([i, j])
        positions_list.append([i, j-1])
        positions_list.append([i-1, j])
        positions_list.append([i, j+1])
        positions_list.append([i+1, j])
    
    return positions_list

def get_neighbour_values(positions_list, matrix):
    values = []
    for i in range(len(positions_list)):
            valor = matrix[positions_list[i][0]][positions_list[i][1]]
            values.append(valor)
    return values

def get_average(numbers):
    '''
    Recibe una lista de números y devuelve su promedio
    '''
    return reduce(lambda accum, x: accum + x, numbers, 0) / len(numbers)