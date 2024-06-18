# Lista de elementos
personas = ["Jesús", 1.70, "Zulema", 1.60, "Fernando", 1.75, "Ysabel", 1.68]

# Actualizar e imprimir elemento en lista
personas[1] = 1.78
print(personas)

# Agregar nuevo elemento en lista
personas = personas + ["Pablo", 1.71]
print(personas)

personas = personas + ["Fabiola", 1.73]
print(personas)

# Eliminar un elemento de la lista (Ysabel)
del(personas[6])
print(personas)

del(personas[6])
print(personas)

# Como funcionan las listas (tanto elementos como personas tienen los mismos elementos)
elementos = personas
print(elementos)
print(personas)

elementos[0] = "Benito"
print(elementos)
print(personas)


# Pasar elementos de una lista a otra (ahora cada lista tiene elementos independientes)
nuevas_personas = list(personas)
nuevas_personas[0] = "Tony"
print(personas)
print(nuevas_personas)
