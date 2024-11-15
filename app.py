from flask import Flask,request,jsonify
#createing s server
app = Flask(__name__) #Creating the server, app is a veriabe here
@app.route('/') # Creating the root server, use postman to send this
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True)
#Flask
app = Flask(__name__)
@app.route('/Piyush',)
def hello_world():
    return 'Hello Piyush'
if __name__ == '__main__':
    app.run(debug=True)
#Calculator
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/calculator/<string:num1>/<string:num2>/<string:operation>', methods=['GET'])
def calculator(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Both num1 and num2 should be numbers.", 400
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed", 400
        result = num1 / num2
    else:
        return "Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.", 400
    return jsonify({
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    })
if __name__ == '__main__':
    app.run(debug=True)

############################################################################## GET TASK GET #################
from flask import Flask, jsonify
app = Flask(__name__)
tasks = [
    {
        "task_id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Pizza, Fruit",
        "done": False
    },
    {
        "task_id": 2,
        "title": "Learn Python",
        "description": "Need to find a good Python tutorial on the web",
        "done": False
    }
]
@app.route('/task/<int:test_id>', methods=['GET'])
def get_task(test_id):
    # Use a for loop to find the task by task_id
    for task in tasks:
        if task["task_id"] == test_id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)