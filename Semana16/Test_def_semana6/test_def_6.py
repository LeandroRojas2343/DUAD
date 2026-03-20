from def_6 import sort_hyphenated_string


def test_with_sort_hyphenated_string(): 
    #Arrange 
    input_text = "python-variable-function-computer-monitor"
    #Act 
    result = sort_hyphenated_string(input_text)
    #Assert 
    assert result == "computer-function-monitor-python-variable"

    
def test_single_word(): 
    #Arrange 
    list_input = "Hello"
    #Act 
    result = sort_hyphenated_string(list_input)
    #Assert
    assert result == "Hello"

    
def test_programming_languages():
    # Arrange 
    input_text = "Python-JavaScript-Rust-Go-Kotlin"
    # Act 
    result = sort_hyphenated_string(input_text)
    # Assert
    assert result == "Go-JavaScript-Kotlin-Python-Rust"