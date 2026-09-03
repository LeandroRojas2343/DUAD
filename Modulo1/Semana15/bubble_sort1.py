def bubble_sort(list): 
    list_length = len(list)

    # Traverse through all elements in the list
    for pass_num in range(list_length): 
        # In each pass, the last element is already in place
        for position in range(0, list_length - pass_num - 1): 
            # If the current element is greater than the next, swap them
            if list[position] > list[position + 1]: 
                list[position], list[position + 1] = list[position + 1], list[position]

# Ask user for list
user_input = input("Enter your list of numbers to sort separated by commas: ")

# Convert input to list of integers
list = [int(x) for x in user_input.split(",")]

# Sort the list
bubble_sort(list)

# Display result
print("Sorted list:", list)