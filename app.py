from flask import Flask, jsonify, request

app = Flask(__name__)

#creating an array of task
tasks = [
    {
        "ID": 1,
        "Title": "Buy groceries",
        "Description": "Fruits, Vegetables, Milk",
        "Done": False,
    },
    {
        "ID": 2,
        "Title": "Do homework",
        "Description": "Math, English, Science",
        "Done": False,
    },
]

#post function
@app.route("/adddata", methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide some data",
        }, 400)
    task = {
        "ID": tasks[-1]["ID"]+1,
        "Title": request.json["Title"],
        "Description": request.json.get("Description", ""),
        "Done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "Success!",
        "message": "Task added successfully!"
    })

@app.route("/getdata")
def gettask():
    return jsonify({
        "data": tasks,
    })

@app.route("/")
def helloworld():
    return "Hello world!"

if __name__ == "__main__":
    app.run(debug = True)