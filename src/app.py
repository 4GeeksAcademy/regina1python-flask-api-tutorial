from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    return 'something'

    """try:
        todos.pop(position)
        return jsonify(todos)
    except IndexError:
        return jsonify({"error": "Índice fuera de rango"}), 404
"""
"""@app.route('/todos', methods=['DELETE'])
def delete_all_todos():
    todos.clear()
  return jsonify(todos)
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
