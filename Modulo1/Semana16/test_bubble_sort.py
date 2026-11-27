from bubble_sort import bubble_sort
import pytest


def test_bubble_sort_with_small_list(): 
    # Arrange
    list_input = [2, 4, 6, 7, 5]
    expected = [2, 4, 5, 6, 7]
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == expected


def test_bubble_sort_with_long_list(): 
    # Arrange
    long_list = list(range(200, 0, -1))  # 200 elements in reverse order
    expected = list(range(1, 201))
    # Act
    result = bubble_sort(long_list)
    # Assert
    assert result == expected


def test_bubble_sort_with_empty_list(): 
    # Arrange
    empty_list = []
    # Act
    result = bubble_sort(empty_list)
    # Assert
    assert result == []


def test_bubble_sort_with_different_parameter_type(): 
    # Arrange
    not_a_list = "Hello"
    # Act and Assert
    with pytest.raises(TypeError): 
        bubble_sort_
