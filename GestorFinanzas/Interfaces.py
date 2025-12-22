import FreeSimpleGUI as sg


def ventana_principal():
    layout = [
        [sg.Text("Gestor de Finanzas", font=("Arial", 18))],

        [sg.Table(
            values=[],
            headings=["Fecha", "Descripción", "Monto", "Categoría", "Tipo"],
            key="TABLA",
            expand_x=True,
            expand_y=True,
            auto_size_columns=True
        )],

        [
            sg.Button("Agregar Categoría"),
            sg.Button("Agregar Ingreso"),
            sg.Button("Agregar Gasto"),
            sg.Button("Salir")
        ]
    ]

    return sg.Window("Finanzas", layout, finalize=True, resizable=True)


def ventana_categoria():
    layout = [
        [sg.Text("Nueva Categoría", font=("Arial", 14))],
        [sg.Text("Nombre"), sg.Input(key="NOMBRE")],
        [
            sg.Radio("Gasto", "TIPO", key="GASTO", default=True),
            sg.Radio("Ingreso", "TIPO", key="INGRESO")
        ],
        [
            sg.Input(key="COLOR", size=(10, 1)),
            sg.ColorChooserButton("Color", target="COLOR")
        ],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]
    return sg.Window("Categoría", layout, modal=True)


def ventana_movimiento(categorias, tipo):
    layout = [
        [sg.Text(f"Nuevo {tipo}", font=("Arial", 14))],
        [sg.Text("Descripción"), sg.Input(key="DESCRIPCION")],
        [sg.Text("Monto"), sg.Input(key="MONTO")],
        [sg.Text("Categoría"), sg.Combo(categorias, key="CATEGORIA", readonly=True)],
        [sg.Text("Fecha (dd/mm/yyyy)"), sg.Input(key="FECHA")],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]
    return sg.Window(tipo, layout, modal=True)
