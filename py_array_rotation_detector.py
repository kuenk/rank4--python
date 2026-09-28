def array_rotation_detector(arr1: list, arr2: list) -> bool:
    """
    Escribe una función en Python que tome dos listas (matrices) como parámetros y determine
    si la segunda lista es una rotación de la primera (hacia la izquierda o hacia la derecha).

    Una rotación significa que los elementos se desplazan de forma circular. Por ejemplo, desplazar 
    [1, 2, 3] a la derecha una posición da como resultado [3, 1, 2].

    La función debe devolver True si arr2 es una rotación de arr1, y False en caso contrario.
    Si las matrices tienen longitudes diferentes, no pueden ser rotaciones entre sí.
    Dos matrices vacías se consideran rotaciones entre sí.
    """
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True
    return False

print(array_rotation_detector([], [1, 2, 3]))  # False
print(array_rotation_detector([1, 2, 3], []))  # False
print(array_rotation_detector([1, 2, 3], [3, 1, 2]))  # True
print(array_rotation_detector([1, 2, 3], [2, 3, 1]))  # True
print(array_rotation_detector([1, 2, 3, 4], [2, 3, 4, 1]))  # True