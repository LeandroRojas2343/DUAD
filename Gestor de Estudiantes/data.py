### data.py ###
import csv
import os

def exportar_csv(lista, archivo):
    try:
        with open(archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["nombre", "seccion", "español", "ingles", "sociales", "ciencias"])
            writer.writeheader()
            for est in lista:
                writer.writerow(est)
        print("\nDatos exportados exitosamente.")
    except Exception as e:
        print(f"Error al exportar: {e}")

def importar_csv(archivo):
    if not os.path.exists(archivo):
        print("\nArchivo no encontrado. Debe exportar primero.")
        return []

    lista = []
    try:
        with open(archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                estudiante = {
                    "nombre": row["nombre"],
                    "seccion": row["seccion"],
                    "español": float(row["español"]),
                    "ingles": float(row["ingles"]),
                    "sociales": float(row["sociales"]),
                    "ciencias": float(row["ciencias"])
                }
                lista.append(estudiante)
        print("\nDatos importados exitosamente.")
    except Exception as e:
        print(f"Error al importar: {e}")
    return lista
