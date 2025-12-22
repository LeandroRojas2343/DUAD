import os
import json
import pytest
from logica import GestorFinanzas
from persistencia import guardar_datos, cargar_datos


def test_guardar_datos_crea_archivo_json():
    # Arrange
    gestor = GestorFinanzas()
    gestor.registrar_movimiento(
        "10/12/2025",
        "Almuerzo",
        3500,
        "Comida",
        "gasto"
    )

    # Act
    guardar_datos(gestor)

    # Assert
    assert os.path.exists("datos.json")


def test_guardar_datos_contenido_correcto():
    # Arrange
    gestor = GestorFinanzas()
    gestor.registrar_movimiento(
        "11/12/2025",
        "Bus",
        1200,
        "Transporte",
        "gasto"
    )

    # Act
    guardar_datos(gestor)

    # Assert
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    assert "categorias" in datos
    assert "movimientos" in datos
    assert len(datos["categorias"]) == 3
    assert len(datos["movimientos"]) == 1



def test_cargar_datos_sin_archivo_no_falla():
    # Arrange
    gestor = GestorFinanzas()

    if os.path.exists("datos.json"):
        os.remove("datos.json")

    # Act
    cargar_datos(gestor)

    # Assert
    assert gestor.lista_categorias != None
    assert gestor.registro_movimientos != None


def teardown_module(module):
    if os.path.exists("datos.json"):
        os.remove("datos.json")
