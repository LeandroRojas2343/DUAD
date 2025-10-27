# linked_list.py

class Nodo: 
    def __init__(self, valor):
        self.valor = valor
        self.next = None


class ListaEnlazada: 
    def __init__(self):
        self.head = None

    def agregar(self, valor): 
        nuevo = Nodo(valor)
        if not self.head: 
            self.head = nuevo 
        else:
            actual = self.head 
            while actual.next:
                actual = actual.next 
            actual.next = nuevo 

    def imprimir(self): 
        actual = self.head 
        while actual: 
            print(actual.valor, end=" -> ")
            actual = actual.next 
        print("None")
        