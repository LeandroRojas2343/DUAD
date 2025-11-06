# bubble_sort.py

def bubble_sort(data):
    """Sorts a list using the Bubble Sort algorithm."""
    # Check the data type
    if not isinstance(data, list):
        raise TypeError("The parameter must be a list.")

    n = len(data)
    # If the list is empty, return an empty list
    if n == 0:
        return []

    # Loop through the list n times
    for i in range(n):
        # On each pass, the last element is already in its correct position
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data
