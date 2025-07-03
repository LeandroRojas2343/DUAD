### menu.py ###
def mostrar_menu_y_obtener_opcion():
    print("\n--- MENÚ ---")
    print("1. Ingresar información de estudiantes")
    print("2. Ver información de todos los estudiantes")
    print("3. Ver top 3 de estudiantes por nota promedio")
    print("4. Ver promedio general de notas")
    print("5. Exportar datos a CSV")
    print("6. Importar datos desde CSV")
    print("7. Salir")

    while True:
        opcion = input("Seleccione una opción válida (1-7): ")
        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
            return int(opcion)
        print("Opción inválida. Intente de nuevo.")
