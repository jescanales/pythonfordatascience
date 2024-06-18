# Listar elementos
numbers = [5, 10, 20, 8, 12, 30, 20, 81]
print(numbers)

# Obtener posición índice de elementos
posicion = numbers.index(20)
print(posicion)

# Obtener el número de veces que aparece 12
contar = numbers.count(20)
print(contar)

# Letras capitales
nombre = "jesús"
letras_capitales = nombre.capitalize()
print(letras_capitales)

# Reemplazar valores
texto_nuevo = nombre.replace("ú", "benito")
print(texto_nuevo)

# Agregar un elemento a la lista
nombres_familia = ["Jesús", "Fernando", "Pablo"]
nombres_familia.append("Benedicto")
print(nombres_familia)

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place_up)
print(place)

# Print out the number of o's in place
print(place.count('o'))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
