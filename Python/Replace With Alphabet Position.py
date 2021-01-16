def alphabet_position(text):
    tx = text.lower()
    aux = ""
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in tx:
        if(x not in a):
            continue
        aux += str(a.index(x)+1)+" "
    return (aux[:-1])
