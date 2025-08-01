from flask import Flask, request, jsonify

app = Flask(__name__)
# users unique: id
# In-memory todo list
todos = [
    {"id": 1, "task": "Buy milk"},
    {"id": 2, "task": "Study Flask"},
    {"id": 3, "task": "Study python"}
]

# Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Add a new todo

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json  # Get JSON data from the request
    todo = {
        "id": len(todos) + 1,  # Simple ID generation
        "task": data["task"]   # Get task from the input
    }
    todos.append(todo)  # Add to list
    return jsonify(todo), 201  # Return new todo with 201 Created

if __name__ == '__main__':
    app.run(debug=True)
