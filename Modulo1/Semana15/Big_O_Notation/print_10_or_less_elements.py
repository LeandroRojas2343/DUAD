def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)
    for index in range(min(list_len, 10)):
        print(list_to_print[index])
        
    
# Complexity: O(1)
# Growth: Constant
# Explanation: Maximum 10 iterations, independent of the list size.