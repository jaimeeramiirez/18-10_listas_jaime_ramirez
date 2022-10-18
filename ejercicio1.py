# Ejercicio 1: Utilice las funciones anteriores para agregar elementos faltantes


def ejercicio1():
    lista = ["P", "t"]
    lista.append("H")
    lista.insert("D")
    lista.extend("I", "J", "K")
    # TODO 
    assert "".join(lista) == "Python"
