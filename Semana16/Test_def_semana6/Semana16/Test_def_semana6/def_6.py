def sort_hyphenated_string(text):
    word_list = text.split('-')
    word_list.sort()
    sorted_string = '-'.join(word_list)
    return sorted_string

# Example
input_text = "python-variable-function-computer-monitor"
result = sort_hyphenated_string(input_text)
print("Sorted string:", result)
