# Elementos para lista
abarrote = "arroz"
prenda = "camisa"
automovil = "camioneta"
celular = "Xiaomi"
computadora = "laptop"

# Lista de elementos 1
lista_elementos = [
    ["Abarrote", abarrote], 
    ["Prenda", prenda], 
    ["Automóvil", automovil], 
    ["Celular", celular], 
    ["Computadora", computadora]
    ]

# Imprimir lista de elementos 1
print(lista_elementos)

# Lista de elementos 2
personas = ["Jesús", 1.70, "Zulema", 1.60, "Fernando", 1.75, "Ysabel", 1.68]

# Sumando elementos de lista personas
suma_talla = (personas[1] + personas[3])
print(suma_talla)

# Imprimir lista de personas
print(personas)

# Obteniendo elemento de lista por su índice
print(lista_elementos[2])
print(personas[2])

# Extrae a partir del tercer elemento hasta el quinto elemento
print(lista_elementos[2:5])

# Extrae apartir del quinto elemento hasta el sexto elemento
print(personas[4:6])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)


