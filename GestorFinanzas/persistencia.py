import json
from logica import Categoria, MovimientoFinanciero


RUTA_ARCHIVO = "datos.json"


def guardar_datos(gestor_finanzas):
    datos = {
        "categorias": [
            {
                "nombre": categoria.nombre,
                "color": categoria.color,
                "tipo": categoria.tipo
            }
            for categoria in gestor_finanzas.lista_categorias
        ],
        "movimientos": [
            {
                "fecha": movimiento.fecha,
                "descripcion": movimiento.descripcion,
                "monto": movimiento.monto,
                "categoria": movimiento.categoria.nombre,
                "tipo": movimiento.tipo
            }
            for movimiento in gestor_finanzas.registro_movimientos
        ]
    }

    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_datos(gestor_finanzas):
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        gestor_finanzas.lista_categorias.clear()
        gestor_finanzas.registro_movimientos.clear()

        for cat in datos["categorias"]:
            gestor_finanzas.lista_categorias.append(
                Categoria(cat["nombre"], cat["color"], cat["tipo"])
            )

        for mov in datos["movimientos"]:
            categoria = gestor_finanzas.buscar_categoria(mov["categoria"])
            gestor_finanzas.registro_movimientos.append(
                MovimientoFinanciero(
                    mov["fecha"],
                    mov["descripcion"],
                    mov["monto"],
                    categoria,
                    mov["tipo"]
                )
            )

    except FileNotFoundError:
        pass

