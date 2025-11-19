import sqlite3
import os

# -------------------------------------------------------
# FUNCIÓN PRINCIPAL DE CONEXIÓN
# -------------------------------------------------------
def obtener_conexion():
    """
    Esta función crea (o abre) un archivo de base de datos SQLite.
    Si el archivo no existe, Python lo crea automáticamente.

    - db_path: ruta donde se guardará la base de datos
    - conn: la conexión abierta hacia ese archivo .db
    """
    db_path = "finanzas.db"
    conexion = sqlite3.connect(db_path)
    return conexion


# -------------------------------------------------------
# CREAR TABLAS SI NO EXISTEN     
# -------------------------------------------------------
def inicializar_tablas():
    """
    Crea las tablas necesarias para el sistema:
    - categorias: contiene las categorías de gastos
    - movimientos: contiene ingresos o gastos con monto, fecha y categoría
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Crear tabla de categorías
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            color TEXT NOT NULL
        )
    """)

    # Crear tabla de movimientos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,        -- 'ingreso' o 'gasto'
            categoria_id INTEGER NOT NULL,   -- 'Transporte' o 'comida'
            monto REAL NOT NULL,
            fecha TEXT NOT NULL,
            descripcion TEXT,                  
                   
        FOREIGN KEY(categoria_id) REFERENCES categorias(id)
        );
    """)

    conexion.commit()
    conexion.close()


# -------------------------------------------------------
# AGREGAR UNA NUEVA CATEGORÍA
# -------------------------------------------------------
def agregar_categoria(nombre, color):
    """
    Agrega una categoría a la tabla "categorias".
    - nombre: nombre de la categoría ("Comida")
    - color: color de la categoría (#FF6B6B)
    """
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO categorias (nombre, color) 
        VALUES (?, ?)
    """, (nombre, color))

    conn.commit()
    conn.close()


# -------------------------------------------------------
# OBTENER TODAS LAS CATEGORÍAS
# -------------------------------------------------------
def obtener_categorias():
    """
    Retorna una lista de todas las categorías guardadas.
    Cada categoría viene como una tupla: (id, nombre, color)
    """
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, color FROM categorias")
    categorias = cursor.fetchall()

    conn.close()
    return categorias


# -------------------------------------------------------
# REGISTRAR UN MOVIMIENTO (ingreso o gasto)
# -------------------------------------------------------
def agregar_movimiento(tipo, categoria_id, monto, fecha, descripcion):
    """
    Guarda un movimiento financiero.
    - tipo: "ingreso" o "gasto"
    - categoria_id: categoría seleccionada
    - monto: número decimal
    - fecha: texto 'YYYY-MM-DD'
    - descripcion: texto opcional
    """
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movimientos (tipo, categoria_id, monto, fecha, descripcion)
        VALUES (?, ?, ?, ?, ?)
    """, (tipo, categoria_id, monto, fecha, descripcion))

    conn.commit()
    conn.close()


# -------------------------------------------------------
# VER TODOS LOS MOVIMIENTOS REGISTRADOS
# -------------------------------------------------------
def obtener_movimientos():
    """
    Retorna todos los movimientos financieros registrados.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT movimientos.id, movimientos.tipo, categorias.nombre, 
               movimientos.monto, movimientos.fecha, movimientos.descripcion
        FROM movimientos
        JOIN categorias ON movimientos.categoria_id = categorias.id
        ORDER BY movimientos.fecha DESC
    """)

    datos = cursor.fetchall()
    conn.close()
    return datos
