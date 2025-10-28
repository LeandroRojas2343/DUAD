def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f'{element_a} {element_b} {element_c}')
                
    return result_list

# Complexity: O(n x m x k)
# Growth: Cubic
# Explanation: Three nested loops (iterates through all possible combinations)