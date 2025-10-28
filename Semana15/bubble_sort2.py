def bubble_sort(lista): 
    longitud_lista = len(lista)
    # Recorremos la lista varias veces
    for pasada in range(longitud_lista):
        # Comparamos cada par de elementos adyacentes
        for posicion in range(longitud_lista - 1, pasada, -1):
            # Si el elemento actual es mayor que el anterior, se intercambian
            if lista[posicion] < lista[posicion - 1]:
                lista[posicion], lista[posicion - 1] = lista[posicion - 1], lista[posicion]

# Pedimos lista de números al usuario
entrada = input("Ingrese su lista de números separados por comas: ")

# Convertimos la entrada en una lista de enteros
entrada = [int(x) for x in entrada.split(",")]

# Llamamos a la función
bubble_sort(entrada)

# Mostramos la lista ordenada
print("Lista ordenada (mayor a menor):", entrada)
