def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    """Escribe una función que encuentre la intersección de varias listas ordenadas. Devuelve una nueva lista que contenga los elementos que aparecen en TODAS las listas de entrada, en orden ordenado.

    La función debe:
    - Devolver los elementos que aparecen en TODAS las listas
    - El resultado debe estar ordenado en orden ascendente
    - Eliminar duplicados del resultado
    - Manejar adecuadamente las entradas vacías o listas vacías
    - Si alguna lista está vacía, la intersección está vacía"""

    result = []
    if lists == []:
        return result

    for elem in lists[0]:
        if elem in result:
            continue
        match = True
        for other in lists[1:]:
            if elem not in other:
                match = False
                break

        if match:
            result.append(elem)

    return result
