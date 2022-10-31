from functools import reduce

def process_list(elements):
    '''
    Recibe una lista de números y devuelve una nueva con los elementos cambiados. Cada elemento de la nueva lista será el promedio del valor antiguo y el de sus vecinos
    '''
    # Creo una lista vacía donde ir acumulando
    processed_list = []

    if len(elements) == 1:
        processed_list = elements
    else:
        # Por cada elemento de la lista...
        for index, element in enumerate(elements):
        # ...lo proceso y
            new_element = process_element(index, elements)
        # lo añado a la lista
            processed_list.append(new_element)

    # Devuelvo la nueva lista
    return processed_list

def  process_element(index, elements):
    '''
    Recibe el índice de un elemento y la lista en la que está, calcula su promedio con sus vecinos y devuelve dicho promedio
    '''
    # Obtengo la lista de vecinos...
    indices = get_neighbor_index(index, elements)
    values = get_neighbor_values(indices, elements)
    # ...calculo su promedio
    avrg = get_average(values)
    # (No) avg = (avg + elements[index]) / 2

    # y devuelvo el valor final
    return avrg

def get_neighbor_index(index, elements):
    '''
    Devuelve la lista de índices de los vecinos, incluido el índice del propio elemento
    '''
    indices = []
    if index == 0:
        # El primero
        indices.append(index + 1)
    elif index == len(elements) - 1:
        # El último
        indices.append(index - 1)
    else:
        indices.append(index + 1)
        indices.append(index - 1)
    # Incluyo el índice del propio elemento
    indices.append(index)

    return indices

def get_neighbor_values(indices, elements):
    values = []
    for index in indices:
        values.append(elements[index])
    return values

def get_average(numbers):
    '''
    Recibe una lista de números y devuelve su promedio
    '''
    return reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers)