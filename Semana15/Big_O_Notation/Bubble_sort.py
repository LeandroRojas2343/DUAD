def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Complejidad: O(n²)
# Crecimiento: Cuadrático
# Explicación: Doble bucle anidado. Ineficiente en listas grandes, usado con fines educativos.