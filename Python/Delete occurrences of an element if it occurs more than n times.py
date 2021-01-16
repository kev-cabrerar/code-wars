def getIndexPositions(listOfElements, element):
    indexPosList = []
    indexPos = 0
    while True:
        try:
            indexPos = listOfElements.index(element, indexPos)
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
    return indexPosList


def delete_nth(order1, max_e):
    # Quitar Duplicados
    order = list(set(order1))
    # Imprimir ultima posición a eliminar
    for x in order:
        a = getIndexPositions(order1, x)
        while (len(a) > max_e):
            # print(a[len(a)-1])
            order1.pop(a[len(a)-1])
            a = getIndexPositions(order1, x)
    return (order1)
