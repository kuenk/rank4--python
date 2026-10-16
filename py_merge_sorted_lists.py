def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    """    Escribe una función que fusione múltiples listas ordenadas en una sola lista ordenada de forma eficiente.

    La función debe:
    - Tomar como entrada una lista de listas de enteros ordenadas
    - Devolver una única lista fusionada en orden ascendente
    - Conservar todos los elementos duplicados en el resultado final
    - Manejar listas vacías y entradas vacías de forma adecuada
    - Mantener una eficiencia óptima para entradas grandes"""

    result = []
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        value, list_index, pos = heapq.heappop(heap)
        result.append(value)
        next_pos = pos + 1
        if next_pos < len(lists[list_index]):
            heapq.heappush(heap, (lists[list_index][next_pos], list_index, next_pos))

    return result
