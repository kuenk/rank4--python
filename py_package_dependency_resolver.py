def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    """
    Escribe una función que determine un orden de instalación de paquetes válido resolviendo dependencias. Usa ordenamiento topológico para garantizar que las dependencias se instalen antes de los paquetes que las requieren.

    La función debe:
    - Tomar un diccionario donde las claves son nombres de paquetes y los valores son listas de dependencias
    - Devolver los paquetes en orden de instalación (dependencias primero)
    - Devolver una lista vacía si no existe un orden válido (dependencias circulares)
    - Manejar entradas vacías y cadenas de dependencias aisladas
    - Ignorar referencias a paquetes que no están en el diccionario de entrada
    """

    degree = {}
    dependents = {}
    for clave in packages.keys():
        degree[clave] = 0
        dependents[clave] = []

    for p, deps in packages.items():
        for d in set(deps):
            if d not in packages:
                continue
            degree[p] += 1
            dependents[d].append(p)

    ready = []
    result = []
    for nombre, contador in degree.items():
        if contador == 0:
            ready.append(nombre)

    while ready:
        ready.sort()
        current = ready.pop(0)
        result.append(current)
        for i in dependents[current]:
            degree[i] -= 1
            if degree[i] == 0:
                ready.append(i)

    if len(result) == len(packages):
        return result
    return []
