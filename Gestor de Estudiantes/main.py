from menu import show_menu_and_get_option
from actions import (
    register_students,
    show_students,
    top_3_students,
    overall_average
)
from data import export_csv, import_csv

students = []

while True:
    option = show_menu_and_get_option()

    if option == 1:
        register_students(students)
    elif option == 2:
        show_students(students)
    elif option == 3:
        top_3_students(students)
    elif option == 4:
        overall_average(students)
    elif option == 5:
        export_csv(students, 'students.csv')
    elif option == 6:
        students = import_csv('students.csv')
    elif option == 7:
        print("Exiting the program...")
        break


