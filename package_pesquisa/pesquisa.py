def pesquisa_sequencial_lista_ordenada(lista, item):
    """
    Realiza uma pesquisa sequencial numa lista ordenada para encontrar o 'item' desejado.

    Args:
    lista (list): A lista ordenada de números a ser pesquisada.
    item: O número que desejamos encontrar na lista.

    Returns:
    bool: Retorna True se o 'item' for encontrado na lista, False caso contrário.
    """
    encontrado = False
    for elemento in lista:
        if elemento == item:
            encontrado = True
            break
        if elemento > item:
            encontrado = False
            break
    return encontrado

def pesquisa(lista, n_vezes):
    """
    Realiza uma pesquisa sequencial recursiva numa lista para encontrar o valor 'n' desejado.

    Args:
    lista (list): A lista de números a ser pesquisada.
    n_vezes: O número que desejamos encontrar na lista.

    Returns:
    bool: Retorna True se o valor 'n' for encontrado na lista, False caso contrário.
    """
    if not lista:  # Condição de parada: lista vazia, elemento não encontrado
        return False
    if lista[0] == n_vezes:
        return True
    return pesquisa(lista[1:], n_vezes)


def pesquisa_binaria(lista, item):
    """
    Realiza uma pesquisa binária numa lista ordenada para encontrar o valor 'item' desejado.

    Args:
    lista (list): A lista ordenada de números a ser pesquisada.
    item: O valor que desejamos encontrar na lista.

    Returns:
    bool: Retorna True se o valor 'item' for encontrado na lista, False caso contrário.
    """
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == item:
            return True
        else:
            if item < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False


def pesquisa_binaria_recursiva(lista, item):
    """
    Realiza uma pesquisa binária recursiva numa lista ordenada para encontrar o valor 'item' desejado.

    Args:
    lista (list): A lista ordenada de números a ser pesquisada.
    item: O valor que desejamos encontrar na lista.

    Returns:
    bool: Retorna True se o valor 'item' for encontrado na lista, False caso contrário.
    """
    if len(lista) == 0:
        return False
    else:
        meio = len(lista) // 2
        if lista[meio] == item:
            return True
        else:
            if item < lista[meio]:
                return pesquisa_binaria_recursiva(lista[:meio], item)
            else:
                return pesquisa_binaria_recursiva(lista[meio + 1:], item)