def palindrome_partitioner(s: str) -> int:
    """
    Dada una cadena s, encuentra el número mínimo de cortes necesarios para particionarla de manera que cada subcadena resultante sea un palíndromo.

    - Devuelve el número mínimo de cortes (un entero)
    - Una cadena de longitud 1 requiere 0 cortes
    - Una cadena vacía requiere 0 cortes"""
    n = len(s)
    cut = [0] * (n + 1)

    for j in range(1, n + 1):
        if is_palindrome(s[:j]):
            cut[j] = 0
            continue
        best = j - 1
        for i in range(1, j):
            if is_palindrome(s[i:j]):
                option = cut[i] + 1
                if option < best:
                    best = option
        cut[j] = best

    return cut[n]
