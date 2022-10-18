lista = list("Python is awesome")

# Mostrar la lista
print("lista = ", lista)
# acceso a un miembro de la lista (get)
print("lista[4] = ", lista[4])
print("lista[-3] = ", lista[-3])

# extracción de sub-lista
print("lista[:6] = ", lista[:6])
print("lista[7:9] = ", lista[7:9])
print("lista[10:] = ", lista[10:])
print("lista[2::5] = ", lista[2::5])
print("lista[-3::-6] = ", lista[-3::-6])

# escritura de un miembro de la lista (set)
lista[11] = "b"
print("""lista[11] = "b" """)
print("lista = ", lista)

print("""lista[13:15] = "fg" """)
lista[13:15] = "fg"
print("lista = ", lista)

# eliminar un miembro de la lista (del)
print("""del lista[15]""")
del lista[15]
print("lista = ", lista)

print("""lista.remove("y")""")
lista.remove("y")
print("lista = ", lista)

print("""while " " in lista: lista.remove(" ")""")
while " " in lista:
    lista.remove(" ")
print("lista = ", lista)

print("""del lista[:7]""")
del lista[:7]
print("lista = ", lista)

# Eliminar el último elemento (y devolverlo)
print("""lista.pop() -> Devuelve :""", lista.pop())
print("lista = ", lista)

# Agregar un elemento al final de la lista
print("""lista.append("h")""")
lista.append("h")
print("lista = ", lista)

# Agregar un elemento en cualquier lugar de la lista
print("""lista.insert(2, "d")""")
lista.insert(2, "d")
print("lista = ", lista)

print("""lista.insert(2, "c")""")
lista.insert(2, "c")
print("lista = ", lista)

# Concatenación de una lista
print("""lista.extend(["i", "j"])""")
lista.extend(["i", "j"])
print("lista = ", lista)

respuesta=print(input("Que ejercicio quieres que te muestre?:"))

if respuesta==1:
  import ejercicio1
elif respuesta==2:
  import ejercicio2
else:
  print("Respuesta incorrecta")
