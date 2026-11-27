# Lyfter Car Rental — Backend

Proyecto completo: base de datos PostgreSQL + API REST en Python (Flask),
probado con pgAdmin y Postman.

```
lyfter_car_rental/
├── sql/
│   ├── 01_create_schema.sql          Tarea 1.1 - crea el schema
│   ├── 02_users_table_seed.sql       Tarea 1.2 - tabla usuarios + 50 registros
│   ├── 03_cars_table_seed.sql        Tarea 1.3 - tabla autos + 30 registros
│   ├── 04_rentals_table.sql          Tarea 1.4 - tabla cruz alquileres
│   └── 05_test_scripts.sql           Tarea 2   - scripts de prueba manuales
├── api/
│   ├── app.py                        Tarea 3   - API Flask (todos los endpoints)
│   ├── db.py                         Conexion + queries parametrizadas
│   ├── requirements.txt
│   └── .env.example
└── postman/
    └── Lyfter_Car_Rental.postman_collection.json
```

Todos los scripts y el API fueron probados de punta a punta contra una
instancia real de PostgreSQL antes de la entrega (50 usuarios y 30 autos
sembrados, alquiler creado, completado, usuario flageado como moroso,
auto deshabilitado, filtros de listado, etc.).

---

## 1. Base de datos (pgAdmin)

1. Abrir pgAdmin, conectarse a su servidor PostgreSQL.
2. Abrir el **Query Tool** sobre la base donde va a trabajar (ej. `postgres`).
3. Ejecutar los scripts **en este orden exacto**:
   1. `sql/01_create_schema.sql`
   2. `sql/02_users_table_seed.sql`
   3. `sql/03_cars_table_seed.sql`
   4. `sql/04_rentals_table.sql`
4. Cada script de tabla es autocontenido: crea la tabla (con `DROP TABLE IF EXISTS`
   primero para poder re-ejecutarlo) y la puebla en la misma corrida.
5. `sql/05_test_scripts.sql` contiene los queries de la Tarea 2. Reemplace los
   valores `<<...>>` con datos reales y ejecute bloque por bloque en pgAdmin
   para probar la base manualmente antes de usar el API.

> Nota: si su base de datos no se llama `postgres`, no hay problema — el schema
> `lyfter_car_rental` se crea dentro de cualquier base a la que se conecte.

---

## 2. API (Python / Flask)

### Instalación

```bash
cd api
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # y editar con las credenciales de su Postgres
```

`.env`:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_SCHEMA=lyfter_car_rental
```

### Ejecución

```bash
python3 app.py
```

El API queda disponible en `http://localhost:5000`.

### Endpoints

**Creación**
| Método | Ruta | Body |
|---|---|---|
| POST | `/users` | `full_name, email, username, password, birth_date, status?` |
| POST | `/cars` | `brand, model, manufacture_year, status?` |
| POST | `/rentals` | `user_id, car_id` (valida que el auto esté disponible y el usuario no esté suspendido/moroso) |

**Modificación**
| Método | Ruta | Body |
|---|---|---|
| PATCH | `/cars/<id>/status` | `{"status": "available\|rented\|disabled\|maintenance"}` |
| PATCH | `/cars/<id>/disable` | — (atajo con regla de negocio: no deshabilita autos alquilados) |
| PATCH | `/users/<id>/status` | `{"status": "active\|inactive\|suspended\|delinquent"}` |
| PATCH | `/users/<id>/flag-delinquent` | — (marca al usuario como moroso) |
| PATCH | `/rentals/<id>/complete` | — (auto → available, alquiler → completed, `return_date` autogenerada) |
| PATCH | `/rentals/<id>/status` | `{"status": "active\|completed\|cancelled"}` |

**Listado (todos con filtros dinámicos por query params)**
| Método | Ruta | Ejemplo |
|---|---|---|
| GET | `/users` | `/users?username=juanperez` |
| GET | `/cars` | `/cars?model=Corolla&status=available` |
| GET | `/rentals` | `/rentals?status=active&user_id=3` |
| GET | `/cars/rented` | atajo directo a autos alquilados |
| GET | `/cars/available` | atajo directo a autos disponibles |

Los filtros de texto (`full_name`, `email`, `username`, `brand`, `model`) hacen
match parcial (`ILIKE`); el resto de columnas hacen match exacto. Solo se
aceptan columnas reales de cada tabla (whitelist en `db.py`), por lo que no
hay riesgo de SQL injection ni por valores ni por nombres de columna.

---

## 3. Postman

Importar `postman/Lyfter_Car_Rental.postman_collection.json` en Postman.
Contiene una carpeta por cada sección (Creación / Modificación / Listado)
con un request de ejemplo por endpoint, usando la variable `{{base_url}}`
(por defecto `http://localhost:5000`).

Flujo sugerido de prueba:
1. `Creacion > Crear usuario` y `Creacion > Crear auto`.
2. `Creacion > Crear alquiler` con los IDs devueltos.
3. `Modificacion > Completar alquiler`.
4. `Listado > *` para verificar los filtros.
