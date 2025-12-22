import pytest 
from logica import Categoria, MovimientoFinanciero, GestorFinanzas 


def test_crear_una_categoria(): 
    #Arrange
    nombre = "Comida"
    color = "#FFA500"
    tipo = "gasto"

    #Act 
    categoria = Categoria(nombre, color, tipo)

    #Assert 
    assert categoria.nombre == "Comida"
    assert categoria.color == "#FFA500"
    assert categoria.tipo == "gasto"


def test_crear_gestor_con_categorias_predeterminadas(): 
    #Arrange 
    gestor = GestorFinanzas()

    #Act 
    categorias = gestor.lista_categorias 

    #Assert 
    assert len(categorias) == 3 
    assert categorias[0].nombre == "Comida"
    assert categorias[1].nombre == "Transporte"
    assert categorias[2].nombre == "Salario"


def test_agregar_categoria_nueva(): 
    #Arrange 
    gestor = GestorFinanzas()

    #Act 
    categoria = gestor.agregar_categoria("Salud", "#FF0000", "gasto")

    #Assert 
    assert categoria.nombre == "Salud"
    assert categoria.color == "#FF0000"
    assert categoria.tipo == "gasto"
    assert len(gestor.lista_categorias) == 4 


def test_agregar_categoria_duplicada_lanza_error(): 
    #Arrange 
    gestor = GestorFinanzas()

    #Act / Assert 
    with pytest.raises(ValueError): 
        gestor.agregar_categoria("Comida", "#FFFFFF", "gasto")


def test_buscar_categoria_existente(): 
    #Arrange 
    gestor = GestorFinanzas()

    #Act 
    categoria = gestor.buscar_categoria("Comida")

    #Assert 
    assert categoria is not None
    assert categoria.nombre == "Comida"


def test_buscar_categoria_inexistente(): 
    #Arrange 
    gestor = GestorFinanzas()

    #Act 
    categoria = gestor.buscar_categoria("Viajes")

    #Assert
    assert categoria is None


def test_registrar_movimiento_valido(): 
    #Arrange 
    gestor = GestorFinanzas()

    #Act 
    movimiento = gestor.registrar_movimiento(
        "10/12/2025", 
        "Almuerzo", 
        3500,
        "Comida", 
        "gasto"
    )

    #Assert 
    assert isinstance(movimiento, MovimientoFinanciero)
    assert movimiento.descripcion == "Almuerzo"
    assert movimiento.monto == 3500 
    assert movimiento.tipo == "gasto"
    assert len(gestor.registro_movimientos) == 1 


def test_registrar_movimiento_con_monto_negativo():
    # Arrange
    gestor = GestorFinanzas()

    # Act / Assert
    with pytest.raises(ValueError):
        gestor.registrar_movimiento(
            "10/12/2025",
            "Error",
            -100,
            "Comida",
            "gasto"
        )


def test_registrar_movimiento_con_fecha_invalida():
    # Arrange
    gestor = GestorFinanzas()

    # Act / Assert
    with pytest.raises(ValueError):
        gestor.registrar_movimiento(
            "2025-12-10",
            "Fecha mala",
            1000,
            "Comida",
            "gasto"
        )


def test_registrar_movimiento_con_categoria_inexistente():
    # Arrange
    gestor = GestorFinanzas()

    # Act / Assert
    with pytest.raises(ValueError):
        gestor.registrar_movimiento(
            "10/12/2025",
            "Algo",
            1000,
            "Viajes",
            "gasto"
        )
