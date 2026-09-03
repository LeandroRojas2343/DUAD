import FreeSimpleGUI as sg


def main_window():
    layout = [
        [sg.Text("Finance Manager", font=("Arial", 18))],

        [sg.Table(
            values=[],
            headings=["Date", "Description", "Amount", "Category", "Type"],
            key="TABLE",
            expand_x=True,
            expand_y=True,
            auto_size_columns=True
        )],

        [
            sg.Button("Add Category"),
            sg.Button("Add Income"),
            sg.Button("Add Expense"),
            sg.Button("Exit")
        ]
    ]

    return sg.Window("Finance", layout, finalize=True, resizable=True)


def category_window(manager):
    layout = [
        [sg.Text("New Category", font=("Arial", 14))],
        [sg.Text("Name"), sg.Input(key="NAME")],
        [
            sg.Radio("Expense", "TYPE", key="EXPENSE", default=True),
            sg.Radio("Income", "TYPE", key="INCOME")
        ],
        [
            sg.Input(key="COLOR", size=(10, 1)),
            sg.ColorChooserButton("Color", target="COLOR")
        ],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    window = sg.Window("Category", layout, modal=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancel"):
            break

        if event == "Save":
            name = values["NAME"].strip()

            if not name:
                sg.popup_error("The name cannot be empty")
                continue

            category_type = "expense" if values["EXPENSE"] else "income"
            color = values["COLOR"]

            try:
                manager.add_category(name, color, category_type)
                sg.popup("Category added successfully")
                break

            except ValueError as e:
                sg.popup_error(e)

    window.close()


def transaction_window(manager, categories, transaction_type):
    layout = [
        [sg.Text(f"New {transaction_type.capitalize()}", font=("Arial", 14))],

        [sg.Text("Description"), sg.Input(key="DESCRIPTION")],

        [sg.Text("Amount"), sg.Input(key="AMOUNT")],

        [
            sg.Text("Category"),
            sg.Combo(
                categories,
                key="CATEGORY",
                readonly=True,
                default_value=""
            )
        ],

        [
            sg.Text("Date"),
            sg.Input(
                key="DATE",
                size=(12, 1),
                disabled=True,
                disabled_readonly_background_color="white"
            ),
            sg.CalendarButton(
                "📅 Select",
                target="DATE",
                format="%d/%m/%Y"
            )
        ],

        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    window = sg.Window(transaction_type.capitalize(), layout, modal=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancel"):
            break

        if event == "Save":
            try:
               

                if not values["DESCRIPTION"] or values["DESCRIPTION"].strip() == "":
                    raise ValueError("The description cannot be empty")

                if not values["AMOUNT"] or values["AMOUNT"].strip() == "":
                    raise ValueError("The amount cannot be empty")

                if values["CATEGORY"] is None:
                    raise ValueError("You must select a category")

                if not values["DATE"] or values["DATE"].strip() == "":
                    raise ValueError("You must select a date")

                # -------- LOGIC -------- #

                manager.register_movement(
                    values["DATE"],
                    values["DESCRIPTION"],
                    values["AMOUNT"],
                    values["CATEGORY"],
                    transaction_type
                )

                sg.popup("Transaction recorded successfully")
                break

            except ValueError as error:
                sg.popup_error(error)

    window.close()
