"""
db.py
Capa de acceso a datos para el API de Lyfter Car Rental.
Usa psycopg2 con un connection pool contra PostgreSQL.
"""

import os
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_SCHEMA = os.getenv("DB_SCHEMA", "lyfter_car_rental")

_pool = psycopg2.pool.SimpleConnectionPool(
    1, 10,
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    options=f"-c search_path={DB_SCHEMA},public",
)


def get_conn():
    return _pool.getconn()


def put_conn(conn):
    _pool.putconn(conn)


def run_query(query, params=None, fetch=True, fetch_one=False):
    """
    Ejecuta una query parametrizada (protegida contra SQL injection).
    fetch=True  -> devuelve filas (SELECT / RETURNING)
    fetch=False -> solo ejecuta (INSERT/UPDATE sin RETURNING)
    """
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params or ())
            if fetch:
                rows = cur.fetchall()
                conn.commit()
                if fetch_one:
                    return rows[0] if rows else None
                return rows
            conn.commit()
            return None
    except Exception:
        conn.rollback()
        raise
    finally:
        put_conn(conn)


# -------------------------------------------------------------------
# Whitelists de columnas filtrables por tabla (Tarea 3 - Listados)
# Solo se permite filtrar por columnas reales de cada tabla, para
# evitar SQL injection via nombres de columna arbitrarios.
# -------------------------------------------------------------------
FILTERABLE_COLUMNS = {
    "users": {"user_id", "full_name", "email", "username", "status", "birth_date"},
    "cars": {"car_id", "brand", "model", "manufacture_year", "status"},
    "rentals": {"rental_id", "user_id", "car_id", "status", "rental_date", "return_date"},
}


def build_filtered_select(table, filters: dict, order_by=None, select_columns="*"):
    """
    Construye dinamicamente un SELECT ... FROM <table> WHERE ... usando
    solo columnas permitidas (whitelist) y parametros bindeados (%s),
    por lo que es seguro ante SQL injection tanto en valores como en
    nombres de columna.
    select_columns: "*" o lista de columnas a devolver (para excluir
    columnas sensibles como password).
    """
    allowed = FILTERABLE_COLUMNS.get(table, set())
    clauses = []
    params = []

    for key, value in filters.items():
        if key not in allowed or value in (None, ""):
            continue
        # texto -> match parcial insensible a mayusculas (LIKE)
        # numerico / status / fechas -> match exacto
        if key in ("full_name", "email", "username", "brand", "model"):
            clauses.append(f"{key} ILIKE %s")
            params.append(f"%{value}%")
        else:
            clauses.append(f"{key} = %s")
            params.append(value)

    columns = select_columns if select_columns == "*" else ", ".join(select_columns)
    query = f"SELECT {columns} FROM {table}"
    if clauses:
        query += " WHERE " + " AND ".join(clauses)
    if order_by:
        query += f" ORDER BY {order_by}"
    return query, params
