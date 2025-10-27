def bubble_sort(lista): 
    longitud_lista = len(lista)

    # Recorremos toda la lista 
    for pasada in range(longitud_lista): 
        # En cada pasada el último elemento ya queda en su lugar 
        for posicion in range(0, longitud_lista - pasada - 1): 
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[posicion] > lista[posicion + 1]: 
                lista[posicion], lista[posicion + 1] = lista[posicion + 1], lista[posicion]

# Pedir lista al usuario
entrada = input("Ingrese su lista de números a ordenar separados por comas: ")

# Convertir la entrada a lista de enteros
lista = [int(x) for x in entrada.split(",")]

# Ordenar la lista
bubble_sort(lista)

# Mostrar resultado
print("Lista ordenada:", lista)