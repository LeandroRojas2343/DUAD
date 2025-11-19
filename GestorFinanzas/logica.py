import persistencia

class Categoria:
    def __init__(self, nombre_categoria, color_categoria):
        self.nombre = nombre_categoria
        self.color = color_categoria
    
    def __str__(self):
        return f"{self.nombre} ({self.color})"
 

class MovimientoFinanciero:
    def __init__(self, fecha_movimiento, descripcion_movimiento, monto_movimiento, categoria_movimiento, tipo_movimiento):
        self.fecha = fecha_movimiento
        self.titulo = descripcion_movimiento
        self.monto = monto_movimiento
        self.categoria = categoria_movimiento
        self.tipo = tipo_movimiento

    def __str__(self):
        return f"{self.fecha} - {self.titulo}: ${self.monto} ({self.categoria.nombre})"


class GestorFinanzas:
    def __init__(self):
        self.lista_categorias = []
        self.registro_movimientos = []
        self._inicializar_categorias_predeterminadas()

    def _inicializar_categorias_predeterminadas(self):
    
        categorias_predeterminadas = [
            # (Nombre categoría, Color identificador)
            ("Comida", "#FF6B6B"),           # Gastos en alimentación
            ("Transporte", "#4ECDC4"),       # Gastos en movilidad
            ("Entretenimiento", "#45B7D1"),  # Gastos en ocio y diversión
            ("Salario", "#96CEB4"),          # Ingresos por trabajo
            ("Servicios", "#FECA57"),        # Gastos en servicios básicos
            ("Compras", "#FF9FF3")           # Gastos en compras varias
        ]

        for nombre_categoria, color_categoria in categorias_predeterminadas:
            self.agregar_categoria(nombre_categoria, color_categoria)

    def _validar_monto(self, monto_a_validar):
      
        try:
            monto_convertido = float(monto_a_validar)
            if monto_convertido <= 0:
                raise ValueError("El monto debe ser mayor a 0")
            return monto_convertido
        except (ValueError, TypeError):
            raise ValueError("El monto debe ser un número válido")

    def _validar_fecha(self, fecha_a_validar):
        try:
            #Guardamos los datos en variables separadas
            dia, mes, anio = map(int, fecha_a_validar.split('/'))
            
            # Verificar formato básico (debe tener exactamente 3 partes)
            if len(fecha_a_validar.split('/')) != 3:
                raise ValueError("Formato de fecha debe ser dd/mm/yyyy")
            
            # Validar rangos básicos de mes y día
            if mes < 1 or mes > 12:
                raise ValueError("El mes debe estar entre 1 y 12")
            if dia < 1 or dia > 31:
                raise ValueError("El día debe estar entre 1 y 31")
            
            # Definir meses con diferentes cantidades de días
            meses_con_31_dias = [1, 3, 5, 7, 8, 10, 12]  # Enero, Marzo, Mayo, etc.
            meses_con_30_dias = [4, 6, 9, 11]            # Abril, Junio, Septiembre, etc.
            
            # Validar días según el mes
            if mes in meses_con_31_dias and dia > 31:
                raise ValueError("Este mes no puede tener más de 31 días")
            elif mes in meses_con_30_dias and dia > 30:
                raise ValueError("Este mes no puede tener más de 30 días")
            elif mes == 2 and dia > 29:  # Febrero
                raise ValueError("Febrero no puede tener más de 29 días")
                
            return fecha_a_validar
        except ValueError as error:
            raise ValueError(f"Fecha inválida: {str(error)}")

    def _verificar_existencia_categoria(self, nombre_categoria_a_verificar):
        """
        Verifica si una categoría ya existe en el sistema
        Compara nombres ignorando mayúsculas/minúsculas para evitar duplicados
        """
        return any(
            categoria_existente.nombre.lower() == nombre_categoria_a_verificar.lower() 
            for categoria_existente in self.lista_categorias
        )

    def _buscar_categoria_por_nombre(self, nombre_categoria_a_buscar):
        """
        Busca y retorna una categoría por su nombre
        Retorna None si no encuentra la categoría solicitada
        """
        for categoria_en_lista in self.lista_categorias:
            if categoria_en_lista.nombre.lower() == nombre_categoria_a_buscar.lower():
                return categoria_en_lista
        return None

    def agregar_categoria(self, nombre_categoria, color_categoria):
        """
        Agrega una nueva categoría al sistema si no existe previamente
        """
        if not self._verificar_existencia_categoria(nombre_categoria):
            nueva_categoria = Categoria(nombre_categoria, color_categoria)
            self.lista_categorias.append(nueva_categoria)
            return nueva_categoria
        else:
            raise ValueError(f"La categoría '{nombre_categoria}' ya existe")

    def registrar_movimiento(self, fecha, descripcion, monto, nombre_categoria, tipo):
        """
        Registra un nuevo movimiento financiero después de validar todos los datos
        """
        # Validaciones previas al registro
        monto_validado = self._validar_monto(monto)
        fecha_validada = self._validar_fecha(fecha)
        categoria_encontrada = self._buscar_categoria_por_nombre(nombre_categoria)
        
        if not categoria_encontrada:
            raise ValueError(f"Categoría '{nombre_categoria}' no encontrada")
        
        if tipo not in ["ingreso", "gasto"]:
            raise ValueError("El tipo debe ser 'ingreso' o 'gasto'")
        
        # Crear y almacenar el movimiento
        nuevo_movimiento = MovimientoFinanciero(
            fecha_validada, 
            descripcion, 
            monto_validado, 
            categoria_encontrada, 
            tipo
        )
        self.registro_movimientos.append(nuevo_movimiento)
        return nuevo_movimiento
