from datetime import datetime


class Categoria:
    def __init__(self, nombre_categoria, color_categoria, tipo_categoria):
        self.nombre = nombre_categoria
        self.color = color_categoria
        self.tipo = tipo_categoria  # ingreso o gasto

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class MovimientoFinanciero:
    def __init__(self, fecha_movimiento, descripcion_movimiento,
                 monto_movimiento, categoria_movimiento, tipo_movimiento):

        self.fecha = fecha_movimiento
        self.descripcion = descripcion_movimiento
        self.monto = monto_movimiento
        self.categoria = categoria_movimiento
        self.tipo = tipo_movimiento

    def __str__(self):
        return f"{self.fecha} | {self.descripcion} | ₡{self.monto}"


class GestorFinanzas:
    def __init__(self):
        self.lista_categorias = []
        self.registro_movimientos = []
        self._crear_categorias_predeterminadas()

    # ---------------- CATEGORÍAS ---------------- #

    def _crear_categorias_predeterminadas(self):
        categorias_base = [
            ("Comida", "#FFA500", "gasto"),
            ("Transporte", "#00CED1", "gasto"),
            ("Salario", "#32CD32", "ingreso")
        ]

        for nombre, color, tipo in categorias_base:
            self.agregar_categoria(nombre, color, tipo)

    def agregar_categoria(self, nombre_categoria, color_categoria, tipo_categoria):
        if self._categoria_existe(nombre_categoria):
            raise ValueError("La categoría ya existe")

        nueva_categoria = Categoria(nombre_categoria, color_categoria, tipo_categoria)
        self.lista_categorias.append(nueva_categoria)
        return nueva_categoria

    def _categoria_existe(self, nombre_categoria):
        return any(
            categoria.nombre.lower() == nombre_categoria.lower()
            for categoria in self.lista_categorias
        )

    def buscar_categoria(self, nombre_categoria):
        for categoria in self.lista_categorias:
            if categoria.nombre.lower() == nombre_categoria.lower():
                return categoria
        return None

    # ---------------- MOVIMIENTOS ---------------- #

    def registrar_movimiento(self, fecha, descripcion, monto, nombre_categoria, tipo_movimiento):
        monto_validado = self._validar_monto(monto)
        fecha_validada = self._validar_fecha(fecha)

        categoria = self.buscar_categoria(nombre_categoria)
        if not categoria:
            raise ValueError("No existe la categoría")

        movimiento = MovimientoFinanciero(
            fecha_validada,
            descripcion,
            monto_validado,
            categoria,
            tipo_movimiento
        )

        self.registro_movimientos.append(movimiento)
        return movimiento

    # ---------------- VALIDACIONES ---------------- #

    def _validar_monto(self, monto):
        monto_convertido = float(monto)
        if monto_convertido <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        return monto_convertido

    def _validar_fecha(self, fecha_texto):
        try:
            datetime.strptime(fecha_texto, "%d/%m/%Y")
            return fecha_texto
        except ValueError:
            raise ValueError("Formato de fecha inválido (dd/mm/yyyy)")
