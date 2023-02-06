from flask import Flask, render_template, jsonify, request, url_for, redirect
import json

app = Flask(__name__)
data = json.load(open("data.json", ))['Students']
print(data)


@app.route('/')
def index():
    return render_template('index.html', data=data)


@app.route("/students")
def students():
    return redirect(url_for('index', data=data))


@app.route('/student/<int:id>')
def student(id):
    student = [std for std in data if std.id == id]
    return render_template('index', student=student)


@app.route('/delete/<int:id>', methods=['DELETE', "GET"])
def delete(id):
    for each in data:
        if each['id'] == int(id):
            data.remove(each)
            return redirect(url_for('index', data=data))
    return redirect(url_for("index", data=data))


@app.route('/edit/<int:id>', methods=['POST', "GET"])
def edit(id):
    student = None
    for each in data:
        if each['id'] == int(id):
            student = each
            break

    if request.method == 'POST':
        newid, name, rollno = request.form['id'], request.form['name'], request.form['rollno']
        for each in data:
            if each['id'] == int(id):
                each['id'] = int(newid)
                each['name'] = name
                each['rollno'] = rollno
                return redirect(url_for('index', data=data))

    return render_template("edit.html", id=student["id"], name=student["name"], rollno=student["rollno"])


@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        id, name, rollno = request.form['id'], request.form['name'], request.form['rollno']
        student = {
            "id": int(id),
            "name": name,
            "rollno": rollno
        }

        data.append(student)
        print(data)

        return redirect(url_for("index", data=data))

    return render_template('add_student.html')


if __name__ == '__main__':
    app.run(debug=True)
