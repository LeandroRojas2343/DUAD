from Funciones import second_function

def test_of_funciones_with_pytest(): 
    # ARRANGE
    expected = None

    # ACT
    result = second_function()

    # ASSERT
    assert result == expected