from datetime import datetime


class Category:
    def __init__(self, category_name, category_color, category_type):
        self.name = category_name
        self.color = category_color
        self.type = category_type  # income or expense

    def __str__(self):
        return f"{self.name} ({self.type})"


class FinancialMovement:
    def __init__(self, movement_date, movement_description,
                 movement_amount, movement_category, movement_type):

        self.date = movement_date
        self.description = movement_description
        self.amount = movement_amount
        self.category = movement_category
        self.type = movement_type

    def __str__(self):
        return f"{self.date} | {self.description} | ₡{self.amount}"


class FinanceManager:
    def __init__(self):
        self.category_list = []
        self.movement_records = []
        self._create_default_categories()

    def _create_default_categories(self):
        base_categories = [
            ("Food", "#FFEE00", "expense"),
            ("Transport", "#00CED1", "expense"),
            ("Salary", "#32CD32", "income")
        ]

        for name, color, category_type in base_categories:
            self.add_category(name, color, category_type)

    def add_category(self, category_name, category_color, category_type):
        category_name = self._validate_text(category_name, "Name")
        category_color = self._validate_text(category_color, "Color")
        category_type = self._validate_text(category_type, "Type")

        if self._category_exists(category_name):
            raise ValueError("The category already exists")

        new_category = Category(category_name, category_color, category_type)
        self.category_list.append(new_category)
        return new_category

    def _category_exists(self, category_name):
        category_name = self._validate_text(category_name, "Category")
        return any(
            category.name.lower() == category_name.lower()
            for category in self.category_list
        )

    def find_category(self, category_name):
        if not category_name:
            return None

        category_name = category_name.strip().lower()
        for category in self.category_list:
            if category.name.lower() == category_name:
                return category
        return None

    def register_movement(self, date, description, amount, category_name, movement_type):

        date = self._validate_date(date)
        description = self._validate_text(description, "Description")
        amount = self._validate_amount(amount)
        category_name = self._validate_text(category_name, "Category")
        movement_type = self._validate_text(movement_type, "Movement type")

        category = self.find_category(category_name)
        if not category:
            raise ValueError("The selected category does not exist")

        movement = FinancialMovement(
            date,
            description,
            amount,
            category,
            movement_type
        )

        self.movement_records.append(movement)
        return movement

    def _validate_text(self, text, field_name):
        if not text or str(text).strip() == "":
            raise ValueError(f"The field '{field_name}' cannot be empty")
        return str(text).strip()

    def _validate_amount(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("The amount must be a valid number")

        if amount <= 0:
            raise ValueError("The amount must be greater than zero")

        return amount

    def _validate_date(self, date_input):
        """
        - Text 'dd/mm/yyyy'
        - Tuple (day, month, year) from FreeSimpleGUI calendar
        return dd/mm/yyyy
        """

        if not date_input:
            raise ValueError("The date cannot be empty")

        # FreeSi Calendar
        if isinstance(date_input, tuple):
            try:
                day, month, year = date_input
                date_obj = datetime(year, month, day)
                return date_obj.strftime("%d/%m/%Y")
            except Exception:
                raise ValueError("Invalid date selected from calendar")

        # Text input case
        if isinstance(date_input, str):
            date_input = date_input.strip()
            if date_input == "":
                raise ValueError("The date cannot be empty")

            try:
                datetime.strptime(date_input, "%d/%m/%Y")
                return date_input
            except ValueError:
                raise ValueError("Invalid date format (dd/mm/yyyy)")

        raise ValueError("Invalid date value")
