import pytest
from def_extra import Operaciones 


def test_division_por_numeros_normales(): 
    #Arrange
    Num_input = Operaciones(10, 2)
    #Act 
    resultado = Num_input.division()
    #Assert 
    assert resultado == 5 


def test_division_por_cero(): 
    #Arrange 
    Num_input = Operaciones(10, 0)
    #Act and assert 
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        Num_input.division()


#Multiplicacion 

def test_normal_para_multiplicacion(): 
    #Arrange 
    Num_input = Operaciones(3, 5)
    #Act
    result = Num_input.multiplicacion()
    #Assert 
    assert result == 15 


def test_con_ceros_multiplicacion(): 
    #Arrange
    List_input = Operaciones(8, 0)
    #Act
    result = List_input.multiplicacion()
    #Assert 
    # Corregido: matemáticamente 8 * 0 = 0
    assert result == 0 


#Promedio 

def test_de_promedio_normal(): 
    #Arrange 
    List_input = Operaciones(8, 4)
    #Act 
    result = List_input.promedio()
    #Assert 
    assert result == 6 


def test_promedio_numeros_negativos(): 
    #Arrange 
    List_input = Operaciones(-10, 0)
    #Act
    result = List_input.promedio()
    #Assert 
    assert result == -5


#Suma 
def test_suma_normal(): 
    #Arrenge 
    List_input = Operaciones(7, 8)
    #Act 
    result = List_input.suma()
    #Assert
    assert result == 15 


def test_suma_negativos(): 
    #Arrenge 
    # Corregido: se deben pasar dos argumentos separados
    List_input = Operaciones(-5, -2)
    #Act 
    result = List_input.suma()
    #Assert 
    assert result == -7


#Conversion 

def test_conversion_grados_fahrenheid(): 
    #Arrange 
    List_input = Operaciones(0, 0)
    #Act 
    resultado = List_input.conversion_grados_a_fahrenheid()
    #Assert 
    assert resultado == 32