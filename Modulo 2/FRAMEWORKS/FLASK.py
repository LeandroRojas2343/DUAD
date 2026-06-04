from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "tasks.json"
VALID_STATUSES = {"To Do", "In Progress", "Completed"}


# Reads the JSON file and returns the list of tasks.
# If the file does not exist yet, returns an empty list.
def read_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# Receives the updated list and writes it to the JSON file.
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


# ──────────────────────────────────────────────
# GET /tasks
# Returns all tasks. If ?status=... is passed,
# filters by that value before responding.
# ──────────────────────────────────────────────
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = read_tasks()
    status = request.args.get("status")

    if status:
        if status not in VALID_STATUSES:
            return jsonify({
                "error": f"Invalid status. Allowed values: {sorted(VALID_STATUSES)}"
            }), 400
        tasks = [t for t in tasks if t["status"] == status]

    return jsonify(tasks), 200


# ──────────────────────────────────────────────
# GET /tasks/<id>
# Looks up a task by its id. If not found, responds 404.
# ──────────────────────────────────────────────
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    tasks = read_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": f"Task with id {task_id} not found"}), 404

    return jsonify(task), 200


# ──────────────────────────────────────────────
# POST /tasks
# Validates all body fields, including that 'id'
# is an integer. If a task with that id already exists, responds 409.
# ──────────────────────────────────────────────
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # All errors are accumulated before responding
    errors = []

    id_value = data.get("id")
    if id_value is None:
        errors.append("The 'id' field is required")
    elif not isinstance(id_value, int):
        errors.append("The 'id' field must be an integer")

    if not data.get("title", "").strip():
        errors.append("The 'title' field is required and cannot be empty")
    if not data.get("description", "").strip():
        errors.append("The 'description' field is required and cannot be empty")
    if not data.get("status", "").strip():
        errors.append("The 'status' field is required")
    elif data["status"] not in VALID_STATUSES:
        errors.append(f"Invalid status. Allowed values: {sorted(VALID_STATUSES)}")

    if errors:
        return jsonify({"errors": errors}), 400

    tasks = read_tasks()

    if any(t["id"] == id_value for t in tasks):
        return jsonify({"error": f"A task with id {id_value} already exists"}), 409

    new_task = {
        "id":          id_value,
        "title":       data["title"].strip(),
        "description": data["description"].strip(),
        "status":      data["status"],
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


# ──────────────────────────────────────────────
# PUT /tasks/<id>
# Replaces the entire task. All three fields are required:
# if any is missing, the request is rejected with 400.
# ──────────────────────────────────────────────
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    tasks = read_tasks()
    index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)

    if index is None:
        return jsonify({"error": f"Task with id {task_id} not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    errors = []

    if not data.get("title", "").strip():
        errors.append("The 'title' field is required and cannot be empty")
    if not data.get("description", "").strip():
        errors.append("The 'description' field is required and cannot be empty")
    if not data.get("status", "").strip():
        errors.append("The 'status' field is required")
    elif data["status"] not in VALID_STATUSES:
        errors.append(f"Invalid status. Allowed values: {sorted(VALID_STATUSES)}")

    if errors:
        return jsonify({"errors": errors}), 400

    # The resource is rebuilt from scratch with the received data
    updated_task = {
        "id":          task_id,
        "title":       data["title"].strip(),
        "description": data["description"].strip(),
        "status":      data["status"],
    }

    tasks[index] = updated_task
    save_tasks(tasks)

    return jsonify(updated_task), 200


# ──────────────────────────────────────────────
# PATCH /tasks/<id>
# Updates only the fields that are sent in the body.
# ──────────────────────────────────────────────
@app.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    tasks = read_tasks()
    index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)

    if index is None:
        return jsonify({"error": f"Task with id {task_id} not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    task = tasks[index]
    errors = []

    if "title" in data:
        if not data["title"].strip():
            errors.append("The 'title' field cannot be empty")
        else:
            task["title"] = data["title"].strip()

    if "description" in data:
        if not data["description"].strip():
            errors.append("The 'description' field cannot be empty")
        else:
            task["description"] = data["description"].strip()

    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            errors.append(f"Invalid status. Allowed values: {sorted(VALID_STATUSES)}")
        else:
            task["status"] = data["status"]

    if errors:
        return jsonify({"errors": errors}), 400

    tasks[index] = task
    save_tasks(tasks)

    return jsonify(task), 200


# ──────────────────────────────────────────────
# DELETE /tasks/<id>
# Deletes the task if it exists. Responds 204 because
# the operation was successful but there is nothing to return.
# ──────────────────────────────────────────────
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = read_tasks()
    new_list = [t for t in tasks if t["id"] != task_id]

    if len(new_list) == len(tasks):
        return jsonify({"error": f"Task with id {task_id} not found"}), 404

    save_tasks(new_list)
    return jsonify({"message": f"Task with id {task_id} deleted successfully"}), 200


# ──────────────────────────────────────────────
# Global error handlers
# ──────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "HTTP method not allowed on this endpoint"}), 405


if __name__ == "__main__":
    app.run(debug=True)