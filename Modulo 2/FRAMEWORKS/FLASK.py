from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "tareas.json"
ESTADOS_VALIDOS = {"Por Hacer", "En Progreso", "Completada"}


# Lee el archivo JSON y devuelve la lista de tareas.
# Si el archivo todavía no existe, retorna una lista vacía.
def leer_tareas():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# Recibe la lista actualizada y la escribe en el archivo JSON.
def guardar_tareas(tareas):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)


# ──────────────────────────────────────────────
# GET /tareas
# Devuelve todas las tareas. Si se pasa ?estado=...,
# filtra por ese valor antes de responder.
# ──────────────────────────────────────────────
@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    tareas = leer_tareas()
    estado = request.args.get("estado")

    if estado:
        if estado not in ESTADOS_VALIDOS:
            return jsonify({
                "error": f"Estado inválido. Valores permitidos: {sorted(ESTADOS_VALIDOS)}"
            }), 400
        tareas = [t for t in tareas if t["estado"] == estado]

    return jsonify(tareas), 200


# ──────────────────────────────────────────────
# GET /tareas/<id>
# Busca una tarea por su id. Si no existe, responde 404.
# ──────────────────────────────────────────────
@app.route("/tareas/<int:tarea_id>", methods=["GET"])
def obtener_tarea(tarea_id):
    tareas = leer_tareas()
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)

    if not tarea:
        return jsonify({"error": f"Tarea con id {tarea_id} no encontrada"}), 404

    return jsonify(tarea), 200


# ──────────────────────────────────────────────
# POST /tareas
# Valida todos los campos del body, incluyendo que 'id'
# sea un entero. Si ya existe una tarea con ese id, responde 409.
# ──────────────────────────────────────────────
@app.route("/tareas", methods=["POST"])
def crear_tarea():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "El cuerpo de la petición debe ser JSON"}), 400

    # Se acumulan todos los errores antes de responder
    errores = []

    id_valor = datos.get("id")
    if id_valor is None:
        errores.append("El campo 'id' es requerido")
    elif not isinstance(id_valor, int):
        errores.append("El campo 'id' debe ser un entero")

    if not datos.get("titulo", "").strip():
        errores.append("El campo 'titulo' es requerido y no puede estar vacío")
    if not datos.get("descripcion", "").strip():
        errores.append("El campo 'descripcion' es requerido y no puede estar vacío")
    if not datos.get("estado", "").strip():
        errores.append("El campo 'estado' es requerido")
    elif datos["estado"] not in ESTADOS_VALIDOS:
        errores.append(f"Estado inválido. Valores permitidos: {sorted(ESTADOS_VALIDOS)}")

    if errores:
        return jsonify({"errores": errores}), 400

    tareas = leer_tareas()

    if any(t["id"] == id_valor for t in tareas):
        return jsonify({"error": f"Ya existe una tarea con id {id_valor}"}), 409

    nueva_tarea = {
        "id":          id_valor,
        "titulo":      datos["titulo"].strip(),
        "descripcion": datos["descripcion"].strip(),
        "estado":      datos["estado"],
    }

    tareas.append(nueva_tarea)
    guardar_tareas(tareas)

    return jsonify(nueva_tarea), 201


# ──────────────────────────────────────────────
# PUT /tareas/<id>
# Reemplaza la tarea completa. Los tres campos son obligatorios:
# si falta alguno, se rechaza la petición con 400.
# ──────────────────────────────────────────────
@app.route("/tareas/<int:tarea_id>", methods=["PUT"])
def editar_tarea(tarea_id):
    tareas = leer_tareas()
    indice = next((i for i, t in enumerate(tareas) if t["id"] == tarea_id), None)

    if indice is None:
        return jsonify({"error": f"Tarea con id {tarea_id} no encontrada"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"error": "El cuerpo de la petición debe ser JSON"}), 400

    errores = []

    if not datos.get("titulo", "").strip():
        errores.append("El campo 'titulo' es obligatorio y no puede estar vacío")
    if not datos.get("descripcion", "").strip():
        errores.append("El campo 'descripcion' es obligatorio y no puede estar vacío")
    if not datos.get("estado", "").strip():
        errores.append("El campo 'estado' es obligatorio")
    elif datos["estado"] not in ESTADOS_VALIDOS:
        errores.append(f"Estado inválido. Valores permitidos: {sorted(ESTADOS_VALIDOS)}")

    if errores:
        return jsonify({"errores": errores}), 400

    # Se construye el recurso desde cero con los datos recibidos
    tarea_actualizada = {
        "id":          tarea_id,
        "titulo":      datos["titulo"].strip(),
        "descripcion": datos["descripcion"].strip(),
        "estado":      datos["estado"],
    }

    tareas[indice] = tarea_actualizada
    guardar_tareas(tareas)

    return jsonify(tarea_actualizada), 200


# ──────────────────────────────────────────────
# PATCH /tareas/<id>

# ──────────────────────────────────────────────
@app.route("/tareas/<int:tarea_id>", methods=["PATCH"])
def actualizar_tarea(tarea_id):
    tareas = leer_tareas()
    indice = next((i for i, t in enumerate(tareas) if t["id"] == tarea_id), None)

    if indice is None:
        return jsonify({"error": f"Tarea con id {tarea_id} no encontrada"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"error": "El cuerpo de la petición debe ser JSON"}), 400

    tarea = tareas[indice]
    errores = []

    if "titulo" in datos:
        if not datos["titulo"].strip():
            errores.append("El campo 'titulo' no puede estar vacío")
        else:
            tarea["titulo"] = datos["titulo"].strip()

    if "descripcion" in datos:
        if not datos["descripcion"].strip():
            errores.append("El campo 'descripcion' no puede estar vacío")
        else:
            tarea["descripcion"] = datos["descripcion"].strip()

    if "estado" in datos:
        if datos["estado"] not in ESTADOS_VALIDOS:
            errores.append(f"Estado inválido. Valores permitidos: {sorted(ESTADOS_VALIDOS)}")
        else:
            tarea["estado"] = datos["estado"]

    if errores:
        return jsonify({"errores": errores}), 400

    tareas[indice] = tarea
    guardar_tareas(tareas)

    return jsonify(tarea), 200


# ──────────────────────────────────────────────
# DELETE /tareas/<id>
# Elimina la tarea si existe. Responde 204 porque
# la operación fue exitosa pero no hay nada que devolver.
# ──────────────────────────────────────────────
@app.route("/tareas/<int:tarea_id>", methods=["DELETE"])
def eliminar_tarea(tarea_id):
    tareas = leer_tareas()
    nueva_lista = [t for t in tareas if t["id"] != tarea_id]

    if len(nueva_lista) == len(tareas):
        return jsonify({"error": f"Tarea con id {tarea_id} no encontrada"}), 404

    guardar_tareas(nueva_lista)
    return "", 204


# ──────────────────────────────────────────────
# Manejadores de errores globales
# ──────────────────────────────────────────────
@app.errorhandler(404)
def no_encontrado(e):
    return jsonify({"error": "Endpoint no encontrado"}), 404

@app.errorhandler(405)
def metodo_no_permitido(e):
    return jsonify({"error": "Método HTTP no permitido en este endpoint"}), 405


if __name__ == "__main__":
    app.run(debug=True)