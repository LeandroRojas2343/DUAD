import json
from logica import Category, FinancialMovement

FILE_PATH = "data.json"


def save_data(finance_manager):
    data = {
        "categories": [
            {
                "name": category.name,
                "color": category.color,
                "type": category.type
            }
            for category in finance_manager.category_list
        ],
        "movements": [
            {
                "date": movement.date,
                "description": movement.description,
                "amount": movement.amount,
                "category": movement.category.name,
                "type": movement.type
            }
            for movement in finance_manager.movement_records
        ]
    }

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data(finance_manager):
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        finance_manager.category_list.clear()
        finance_manager.movement_records.clear()

        for cat in data["categories"]:
            finance_manager.category_list.append(
                Category(cat["name"], cat["color"], cat["type"])
            )

        for mov in data["movements"]:
            category = finance_manager.find_category(mov["category"])
            finance_manager.movement_records.append(
                FinancialMovement(
                    mov["date"],
                    mov["description"],
                    mov["amount"],
                    category,
                    mov["type"]
                )
            )

    except FileNotFoundError:
        pass
