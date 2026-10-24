
from flask import Flask, render_template, request

app = Flask(__name__)

students = {}


@app.route("/")
def home():
    return render_template("main.html", students=students)


@app.route("/add_student", methods=["POST"])
def add_student():

    name = request.form.get("name")

    if name:
        students[name] = {
            "present": 0,
            "absent": 0
        }

    return render_template("main.html", students=students)


@app.route("/attendance", methods=["POST"])
def attendance():

    name = request.form.get("name")
    status = request.form.get("status")

    if name in students:

        if status == "present":
            students[name]["present"] += 1

        elif status == "absent":
            students[name]["absent"] += 1

    return render_template("main.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)

