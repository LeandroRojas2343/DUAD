def show_menu_and_get_option():
    print("\n--- MENU ---")
    print("1. Enter student information")
    print("2. View all student information")
    print("3. View top 3 students by average grade")
    print("4. View overall average grade")
    print("5. Export data to CSV")
    print("6. Import data from CSV")
    print("7. Exit")

    while True:
        option = input("Select a valid option (1-7): ")
        if option in ["1", "2", "3", "4", "5", "6", "7"]:
            return int(option)
        print("Invalid option. Please try again.")

