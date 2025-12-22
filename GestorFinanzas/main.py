import FreeSimpleGUI as sg
from logica import GestorFinanzas
from persistencia import guardar_datos, cargar_datos
from interfaces import (
    ventana_principal,
    ventana_categoria,
    ventana_movimiento
)


def movimientos_a_tabla(gestor):
    return [
        [
            m.fecha,
            m.descripcion,
            m.monto,
            m.categoria.nombre,
            m.tipo
        ] for m in gestor.registro_movimientos
    ]


def main():
    gestor = GestorFinanzas()
    cargar_datos(gestor)

    ventana = ventana_principal()
    ventana["TABLA"].update(values=movimientos_a_tabla(gestor))

    while True:
        evento, valores = ventana.read()

        if evento in (sg.WIN_CLOSED, "Salir"):
            guardar_datos(gestor)
            break

        if evento == "Agregar Categoría":
            win = ventana_categoria()
            ev, val = win.read()
            win.close()

            if ev == "Guardar":
                tipo = "gasto" if val["GASTO"] else "ingreso"
                gestor.agregar_categoria(val["NOMBRE"], val["COLOR"], tipo)
                guardar_datos(gestor)

        if evento in ("Agregar Ingreso", "Agregar Gasto"):
            tipo = "ingreso" if evento == "Agregar Ingreso" else "gasto"

            categorias = [
                c.nombre for c in gestor.lista_categorias if c.tipo == tipo
            ]

            if not categorias:
                sg.popup_error("No hay categorías disponibles")
                continue

            win = ventana_movimiento(categorias, tipo)
            ev, val = win.read()
            win.close()

            if ev == "Guardar":
                gestor.registrar_movimiento(
                    val["FECHA"],
                    val["DESCRIPCION"],
                    val["MONTO"],
                    val["CATEGORIA"],
                    tipo
                )

                ventana["TABLA"].update(values=movimientos_a_tabla(gestor))
                guardar_datos(gestor)

    ventana.close()


if __name__ == "__main__":
    main()
