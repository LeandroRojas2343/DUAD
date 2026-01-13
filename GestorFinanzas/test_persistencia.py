import os
import json
import pytest
from logica import FinanceManager
from persistencia import save_data, load_data


def test_save_data_creates_json_file():
    # Arrange
    manager = FinanceManager()
    manager.register_movement(
        "10/12/2025",
        "Lunch",
        3500,
        "Food",
        "expense"
    )

    # Act
    save_data(manager)

    # Assert
    assert os.path.exists("data.json")


def test_save_data_has_correct_content():
    # Arrange
    manager = FinanceManager()
    manager.register_movement(
        "11/12/2025",
        "Bus",
        1200,
        "Transport",
        "expense"
    )

    # Act
    save_data(manager)

    # Assert
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    assert "categories" in data
    assert "movements" in data
    assert len(data["categories"]) == 3
    assert len(data["moveme]()
