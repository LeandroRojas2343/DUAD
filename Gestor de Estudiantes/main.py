### main.py ###
from menu import mostrar_menu_y_obtener_opcion
from actions import (
    registrar_estudiantes,
    mostrar_estudiantes,
    top_3_estudiantes,
    promedio_general
)
from data import exportar_csv, importar_csv

estudiantes = []

while True:
    opcion = mostrar_menu_y_obtener_opcion()

    if opcion == 1:
        registrar_estudiantes(estudiantes)
    elif opcion == 2:
        mostrar_estudiantes(estudiantes)
    elif opcion == 3:
        top_3_estudiantes(estudiantes)
    elif opcion == 4:
        promedio_general(estudiantes)
    elif opcion == 5:
        exportar_csv(estudiantes, 'estudiantes.csv')
    elif opcion == 6:
        estudiantes = importar_csv('estudiantes.csv')
    elif opcion == 7:
        print("Saliendo del programa...")
        break

