# Ejercicio 2: Utilice las funciones anteriores para elminar elementos sobrantes

def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    del lista[7]
    lista.remove(8)
    lista.pop()
    # TODO
    assert lista == list(range(1, 6))

ejercicio2()