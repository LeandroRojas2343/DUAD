### actions.py ###
def pedir_nota(materia):
    while True:
        try:
            nota = float(input(f"Nota de {materia}: "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Debe ingresar un número válido.")

def registrar_estudiantes(lista):
    try:
        n = int(input("¿Cuántos estudiantes desea registrar?: "))
    except ValueError:
        print("Debe ingresar un número entero.")
        return

    for _ in range(n):
        print("\n--- Nuevo Estudiante ---")
        nombre = input("Nombre completo: ")
        seccion = input("Sección (ej: 11B): ")
        esp = pedir_nota("Español")
        ing = pedir_nota("Inglés")
        soc = pedir_nota("Sociales")
        cie = pedir_nota("Ciencias")

        estudiante = {
            "nombre": nombre,
            "seccion": seccion,
            "español": esp,
            "ingles": ing,
            "sociales": soc,
            "ciencias": cie
        }

        lista.append(estudiante)


def mostrar_estudiantes(lista):
    if not lista:
        print("\nNo hay estudiantes registrados.")
        return
    for est in lista:
        print("\nNombre:", est['nombre'])
        print("Sección:", est['seccion'])
        print("Español:", est['español'])
        print("Inglés:", est['ingles'])
        print("Sociales:", est['sociales'])
        print("Ciencias:", est['ciencias'])


def top_3_estudiantes(lista):
    if len(lista) < 3:
        print("\nDebe haber al menos 3 estudiantes para ver el top 3.")
        return

    promedios = []
    for est in lista:
        promedio = (est['español'] + est['ingles'] + est['sociales'] + est['ciencias']) / 4
        promedios.append((promedio, est))

    top3 = sorted(promedios, key=lambda x: x[0], reverse=True)[:3]

    print("\n--- Top 3 Estudiantes ---")
    for i, (prom, est) in enumerate(top3, 1):
        print(f"#{i} - {est['nombre']} ({est['seccion']}), Promedio: {prom:.2f}")


def promedio_general(lista):
    if not lista:
        print("\nNo hay estudiantes registrados.")
        return

    suma = 0
    for est in lista:
        suma += (est['español'] + est['ingles'] + est['sociales'] + est['ciencias']) / 4

    promedio = suma / len(lista)
    print(f"\nPromedio general de los estudiantes: {promedio:.2f}")