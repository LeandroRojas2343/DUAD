# bubble_sort_linked.py

from Linked_list import ListaEnlazada  # importamos la clase desde el otro archivo

def bubble_sort_linked(lista):
    """Ordena una lista enlazada con bubble sort"""
    if not lista.head:
        return

    cambiado = True
    while cambiado:
        cambiado = False
        actual = lista.head
        while actual.next:
            if actual.valor > actual.next.valor:
                # Intercambiamos los valores
                actual.valor, actual.next.valor = actual.next.valor, actual.valor
                cambiado = True
            actual = actual.next

# --- Prueba del módulo ---
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar(5)
    lista.agregar(3)
    lista.agregar(8)
    lista.agregar(1)
    lista.agregar(4)

    print("Antes de ordenar:")
    lista.imprimir()

    bubble_sort_linked(lista)

    print("Después de ordenar:")
    lista.imprimir()

    
