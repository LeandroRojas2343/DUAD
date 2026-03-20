import pytest
from def_3 import sum_list
 


def test_of_sum_list(): 
    #Arrange 
    list_input = [4, 6, 2, 29]
    expend = [41]
    #Act
    result = sum_list([4, 6, 2, 29])
    #Assert 
    assert result == 41 


def test_sum_list_with_negative_numbers(): 
    #Arrange 
    list_input = [-4, 10, -5]
    expected = 1
    #Act 
    result = sum_list(list_input)
    #Assert 
    assert result == expected


def test_sum_empty_list(): 
    list_input = []
    expected = 0 
    #Act 
    result = sum_list(list_input)
    #Assert 
    assert result == expected
    

def test_sum_decimal_numbers():
    # Arrange 
    list_input = [299.99, 59.99, 19.99, 9.99] 
    expected = 389.96
    
    # Act
    result = sum_list(list_input)
    
    # Assert
    assert result == expected, "¡El total de la compra tecnológica no cuadra!"


def test_sum_large_sequence():
    # Arrange 
    list_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = 55
    # Act
    result = sum_list(list_input)
    # Assert
    assert result == pytest.approx(expected)