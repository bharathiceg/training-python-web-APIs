from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory task list
tasks = [
    {"id": 1, "title": "Study Flask", "done": False},
    {"id": 2, "title": "Write IDS blog", "done": False}
]

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    new_task = request.get_json()

    if 'title' not in new_task:
        return jsonify({"error": "Missing 'title' in request"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": new_task['title'],
        "done": new_task.get('done', False)
    }

    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True)
