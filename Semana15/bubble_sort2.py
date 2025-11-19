def bubble_sort(list): 
    list_length = len(list)
    # We traverse the list multiple times
    for pass_num in range(list_length):
        # We compare each pair of adjacent elements
        for position in range(list_length - 1, pass_num, -1):
            # If the current element is smaller than the previous one, swap them
            if list[position] < list[position - 1]:
                list[position], list[position - 1] = list[position - 1], list[position]

# Ask user for list of numbers
user_input = input("Enter your list of numbers separated by commas: ")

# Convert input into a list of integers
user_input = [int(x) for x in user_input.split(",")]

# Call the function
bubble_sort(user_input)

# Display the sorted list
print("Sorted list (ascending order):", user_input)