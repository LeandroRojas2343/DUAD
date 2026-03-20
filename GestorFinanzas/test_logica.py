import pytest
from logica import Category, FinancialMovement, FinanceManager


def test_create_category():
    # Arrange
    name = "Food"
    color = "#FFA500"
    category_type = "expense"

    # Act
    category = Category(name, color, category_type)

    # Assert
    assert category.name == "Food"
    assert category.color == "#FFA500"
    assert category.type == "expense"


def test_create_manager_with_default_categories():
    # Arrange
    manager = FinanceManager()

    # Act
    categories = manager.category_list

    # Assert
    assert len(categories) == 3
    assert categories[0].name == "Food"
    assert categories[1].name == "Transport"
    assert categories[2].name == "Salary"


def test_add_new_category():
    # Arrange
    manager = FinanceManager()

    # Act
    category = manager.add_category("Health", "#FF0000", "expense")

    # Assert
    assert category.name == "Health"
    assert category.color == "#FF0000"
    assert category.type == "expense"
    assert len(manager.category_list) == 4


def test_adding_duplicate_category_raises_error():
    # Arrange
    manager = FinanceManager()

    # Act / Assert
    with pytest.raises(ValueError):
        manager.add_category("Food", "#FFFFFF", "expense")


def test_find_existing_category():
    # Arrange
    manager = FinanceManager()

    # Act
    category = manager.find_category("Food")

    # Assert
    assert category is not None
    assert category.name == "Food"


def test_find_non_existing_category():
    # Arrange
    manager = FinanceManager()

    # Act
    category = manager.find_category("Travel")

    # Assert
    assert category is None


def test_register_valid_movement():
    # Arrange
    manager = FinanceManager()

    # Act
    movement = manager.register_movement(
        "10/12/2025",
        "Lunch",
        3500,
        "Food",
        "expense"
    )

    # Assert
    assert isinstance(movement, FinancialMovement)
    assert movement.description == "Lunch"
    assert movement.amount == 3500
    assert movement.type == "expense"
    assert len(manager.movement_records) == 1


def test_register_movement_with_negative_amount():
    # Arrange
    manager = FinanceManager()

    # Act / Assert
    with pytest.raises(ValueError):
        manager.register_movement(
            "10/12/2025",
            "Error",
            -100,
            "Food",
            "expense"
        )


def test_register_movement_with_invalid_date():
    # Arrange
    manager = FinanceManager()

    # Act / Assert
    with pytest.raises(ValueError):
        manager.register_movement(
            "2025-12-10",
            "Bad date",
            1000,
            "Food",
            "expense"
        )


def test_register_movement_with_non_existing_category():
    # Arrange
    manager = FinanceManager()

    # Act / Assert
    with pytest.raises(ValueError):
        manager.register_movement(
            "10/12/2025",
            "Something",
            1000,
            "Travel",
            "expense"
        )
