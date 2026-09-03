import FreeSimpleGUI as sg
from logica import FinanceManager
from persistencia import load_data, save_data
from interfaces import (
    main_window,
    category_window,
    transaction_window
)


def movements_to_table(manager):
    return [
        [
            m.date,
            m.description,
            m.amount,
            m.category.name,
            m.type
        ]
        for m in manager.movement_records
    ]


def main():
    manager = FinanceManager()
    load_data(manager)

    window = main_window()
    window["TABLE"].update(values=movements_to_table(manager))

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            save_data(manager)
            break

        # -------- ADD CATEGORY --------
        if event == "Add Category":
            category_window(manager)

        # -------- ADD INCOME / EXPENSE --------
        elif event in ("Add Income", "Add Expense"):
            transaction_type = "income" if event == "Add Income" else "expense"

            categories = [
                c.name
                for c in manager.category_list
                if c.type == transaction_type
            ]

            if not categories:
                sg.popup_error(
                    f"There are no registered categories for {transaction_type}"
                )
                continue

            transaction_window(manager, categories, transaction_type)

            window["TABLE"].update(
                values=movements_to_table(manager)
            )

    window.close()


if __name__ == "__main__":
    main()
    
 

