"""
app.py
API REST de Lyfter Car Rental (Tarea 3).

Endpoints:
  Creacion
    POST   /users
    POST   /cars
    POST   /rentals
  Modificacion
    PATCH  /cars/<car_id>/status
    PATCH  /users/<user_id>/status
    PATCH  /rentals/<rental_id>/complete
    PATCH  /rentals/<rental_id>/status
    PATCH  /users/<user_id>/flag-delinquent
  Listado (todos aceptan filtros via query params)
    GET    /users?username=...&status=...
    GET    /cars?model=...&status=...
    GET    /rentals?status=...&user_id=...&car_id=...
"""

from flask import Flask, request, jsonify
import psycopg2
import db

app = Flask(__name__)

VALID_USER_STATUSES = {"active", "inactive", "suspended", "delinquent"}
VALID_CAR_STATUSES = {"available", "rented", "disabled", "maintenance"}
VALID_RENTAL_STATUSES = {"active", "completed", "cancelled"}


def error(message, status_code=400):
    return jsonify({"error": message}), status_code


# =====================================================================
# CREACION
# =====================================================================

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(force=True, silent=True) or {}
    required = ["full_name", "email", "username", "password", "birth_date"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return error(f"Campos faltantes: {', '.join(missing)}")

    try:
        row = db.run_query(
            """
            INSERT INTO users (full_name, email, username, password, birth_date, status)
            VALUES (%s, %s, %s, %s, %s, COALESCE(%s, 'active'))
            RETURNING user_id, full_name, email, username, birth_date, status, created_at
            """,
            (data["full_name"], data["email"], data["username"], data["password"],
             data["birth_date"], data.get("status")),
            fetch=True, fetch_one=True,
        )
        return jsonify(row), 201
    except psycopg2.errors.UniqueViolation:
        return error("El email o username ya existe", 409)
    except Exception as e:
        return error(str(e), 500)


@app.route("/cars", methods=["POST"])
def create_car():
    data = request.get_json(force=True, silent=True) or {}
    required = ["brand", "model", "manufacture_year"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return error(f"Campos faltantes: {', '.join(missing)}")

    try:
        row = db.run_query(
            """
            INSERT INTO cars (brand, model, manufacture_year, status)
            VALUES (%s, %s, %s, COALESCE(%s, 'available'))
            RETURNING *
            """,
            (data["brand"], data["model"], data["manufacture_year"], data.get("status")),
            fetch=True, fetch_one=True,
        )
        return jsonify(row), 201
    except Exception as e:
        return error(str(e), 500)


@app.route("/rentals", methods=["POST"])
def create_rental():
    data = request.get_json(force=True, silent=True) or {}
    user_id = data.get("user_id")
    car_id = data.get("car_id")
    if not user_id or not car_id:
        return error("Se requiere user_id y car_id")

    user = db.run_query("SELECT status FROM users WHERE user_id = %s", (user_id,), fetch_one=True)
    if not user:
        return error("Usuario no existe", 404)
    if user["status"] in ("suspended", "delinquent"):
        return error(f"El usuario tiene estado '{user['status']}' y no puede alquilar", 409)

    car = db.run_query("SELECT status FROM cars WHERE car_id = %s", (car_id,), fetch_one=True)
    if not car:
        return error("Auto no existe", 404)
    if car["status"] != "available":
        return error(f"El auto no esta disponible (estado actual: {car['status']})", 409)

    try:
        rental = db.run_query(
            """
            INSERT INTO rentals (user_id, car_id, status)
            VALUES (%s, %s, 'active')
            RETURNING *
            """,
            (user_id, car_id), fetch=True, fetch_one=True,
        )
        db.run_query("UPDATE cars SET status = 'rented' WHERE car_id = %s", (car_id,), fetch=False)
        return jsonify(rental), 201
    except Exception as e:
        return error(str(e), 500)


# =====================================================================
# MODIFICACION
# =====================================================================

@app.route("/cars/<int:car_id>/status", methods=["PATCH"])
def update_car_status(car_id):
    data = request.get_json(force=True, silent=True) or {}
    new_status = data.get("status")
    if new_status not in VALID_CAR_STATUSES:
        return error(f"status debe ser uno de: {sorted(VALID_CAR_STATUSES)}")

    car = db.run_query("SELECT * FROM cars WHERE car_id = %s", (car_id,), fetch_one=True)
    if not car:
        return error("Auto no existe", 404)

    # Regla de negocio: no se puede deshabilitar un auto que esta alquilado
    if new_status == "disabled" and car["status"] == "rented":
        return error("No se puede deshabilitar un auto que esta actualmente alquilado", 409)

    row = db.run_query(
        "UPDATE cars SET status = %s WHERE car_id = %s RETURNING *",
        (new_status, car_id), fetch_one=True,
    )
    return jsonify(row)


@app.route("/cars/<int:car_id>/disable", methods=["PATCH"])
def disable_car(car_id):
    """Endpoint dedicado (Tarea 2, punto 7): deshabilita un auto del alquiler."""
    car = db.run_query("SELECT * FROM cars WHERE car_id = %s", (car_id,), fetch_one=True)
    if not car:
        return error("Auto no existe", 404)
    if car["status"] == "rented":
        return error("No se puede deshabilitar un auto que esta actualmente alquilado", 409)

    row = db.run_query(
        "UPDATE cars SET status = 'disabled' WHERE car_id = %s RETURNING *",
        (car_id,), fetch_one=True,
    )
    return jsonify(row)


@app.route("/users/<int:user_id>/status", methods=["PATCH"])
def update_user_status(user_id):
    data = request.get_json(force=True, silent=True) or {}
    new_status = data.get("status")
    if new_status not in VALID_USER_STATUSES:
        return error(f"status debe ser uno de: {sorted(VALID_USER_STATUSES)}")

    row = db.run_query(
        "UPDATE users SET status = %s WHERE user_id = %s RETURNING *",
        (new_status, user_id), fetch_one=True,
    )
    if not row:
        return error("Usuario no existe", 404)
    return jsonify(row)


@app.route("/users/<int:user_id>/flag-delinquent", methods=["PATCH"])
def flag_user_delinquent(user_id):
    row = db.run_query(
        "UPDATE users SET status = 'delinquent' WHERE user_id = %s RETURNING *",
        (user_id,), fetch_one=True,
    )
    if not row:
        return error("Usuario no existe", 404)
    return jsonify(row)


@app.route("/rentals/<int:rental_id>/complete", methods=["PATCH"])
def complete_rental(rental_id):
    """Confirma la devolucion: auto -> available, alquiler -> completed + return_date."""
    rental = db.run_query("SELECT * FROM rentals WHERE rental_id = %s", (rental_id,), fetch_one=True)
    if not rental:
        return error("Alquiler no existe", 404)
    if rental["status"] != "active":
        return error(f"El alquiler ya esta en estado '{rental['status']}'", 409)

    updated_rental = db.run_query(
        """
        UPDATE rentals
        SET status = 'completed', return_date = CURRENT_TIMESTAMP
        WHERE rental_id = %s
        RETURNING *
        """,
        (rental_id,), fetch_one=True,
    )
    db.run_query(
        "UPDATE cars SET status = 'available' WHERE car_id = %s",
        (rental["car_id"],), fetch=False,
    )
    return jsonify(updated_rental)


@app.route("/rentals/<int:rental_id>/status", methods=["PATCH"])
def update_rental_status(rental_id):
    data = request.get_json(force=True, silent=True) or {}
    new_status = data.get("status")
    if new_status not in VALID_RENTAL_STATUSES:
        return error(f"status debe ser uno de: {sorted(VALID_RENTAL_STATUSES)}")

    row = db.run_query(
        "UPDATE rentals SET status = %s WHERE rental_id = %s RETURNING *",
        (new_status, rental_id), fetch_one=True,
    )
    if not row:
        return error("Alquiler no existe", 404)
    return jsonify(row)


# =====================================================================
# LISTADO (con filtros dinamicos por query params)
# =====================================================================

@app.route("/users", methods=["GET"])
def list_users():
    safe_columns = ["user_id", "full_name", "email", "username", "birth_date", "status", "created_at"]
    query, params = db.build_filtered_select(
        "users", request.args.to_dict(), order_by="user_id", select_columns=safe_columns
    )
    rows = db.run_query(query, params)
    return jsonify(rows)


@app.route("/cars", methods=["GET"])
def list_cars():
    query, params = db.build_filtered_select("cars", request.args.to_dict(), order_by="car_id")
    rows = db.run_query(query, params)
    return jsonify(rows)


@app.route("/rentals", methods=["GET"])
def list_rentals():
    query, params = db.build_filtered_select("rentals", request.args.to_dict(), order_by="rental_id")
    rows = db.run_query(query, params)
    return jsonify(rows)


@app.route("/cars/rented", methods=["GET"])
def list_rented_cars():
    rows = db.run_query("SELECT * FROM cars WHERE status = 'rented' ORDER BY car_id")
    return jsonify(rows)


@app.route("/cars/available", methods=["GET"])
def list_available_cars():
    rows = db.run_query("SELECT * FROM cars WHERE status = 'available' ORDER BY car_id")
    return jsonify(rows)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
