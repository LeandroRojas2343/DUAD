# bubble_sort_linked.py

from Linked_list import LinkedList  # import the class from the other file

def bubble_sort_linked(list):
    """Sorts a linked list using bubble sort"""
    if not list.head:
        return

    changed = True
    while changed:
        changed = False
        current = list.head
        while current.next:
            if current.value > current.next.value:
                # Swap the values
                current.value, current.next.value = current.next.value, current.value
                changed = True
            current = current.next

# --- Module test ---
if __name__ == "__main__":
    list = LinkedList()
    list.add(5)
    list.add(3)
    list.add(8)
    list.add(1)
    list.add(4)

    print("Before sorting:")
    list.print()

    bubble_sort_linked(list)

    print("After sorting:")
    list.print()