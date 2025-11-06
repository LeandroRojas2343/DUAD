from def_6 import sort_hyphenated_string


def test_with_sort_hyphenated_string(): 
    #Arrange 
    input_text = "python-variable-function-computer-monitor"
    #Act 
    result = sort_hyphenated_string(input_text)
    #Assert 
    assert result == "computer-function-monitor-python-variable"

    