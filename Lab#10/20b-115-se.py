from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)

# api = Api(app)
# std_put = reqparse.RequestParser()
# std_put.add_argument("Name", type=str)
# std_put.add_argument("Rollno", type=str)

stds =[
    {"id":"55","Name": "Farhan", "Rollno": "20b-055-se"},
    {"id":"17","Name": "Bajwa", "Rollno": "20b-017-se"},
]


# def find(id):
#     if id not in stds:
#         abort(404, meesage="Student not found!")


# class std(Resource):
#     def get(self, id):
#         find(id)
#         return stds[id]

#     def put(self, id):
#         newstd = std.put.parse_args()
#         stds[id] = newstd
#         return stds[id]

#     def delete(self, id):
#         find(id)
#         del stds[id]
#         return 200,''

# api.add_resource(std,'/show/<int:std_id>')

@app.route("/")
def index():
    return "katau"


@app.route("/show")
def getStudents():
    return jsonify(stds)


@app.route("/show/<int:id>")
def getStudent(id):
    if id in stds:
        return jsonify(stds[id])
    return "not found"


@app.route('/student/add', methods=['POST'])
def addStudent():
    db = request.json
    for each in stds: return "student already exists" if each['id']==db['id'] else ''
    stds.append(db)
    print(stds)
    return "success"

@app.route('/student/remove/<int:id>', methods=['DELETE'])
def removeStudent(id):
    for each in stds:
        if each["id"]==str(id):
            stds.remove(each)
            break
        else:
            return "Not found"
    print(stds)
    return "student deleted"



if __name__ == "__main__":
    app.run(debug=True)
