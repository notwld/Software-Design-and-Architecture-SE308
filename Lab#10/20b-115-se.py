from flask import Flask
from flask_restful import Api,Resource,reqparse,abort

app = Flask(__name__)
API = Api(app)

student_put = reqparse.RequestParser()
student_put.add_argument("Name",type=str,location="form")
student_put.add_argument("Rollno",type=str,location="form")

students = {
    1:{"name":"bajwa","rollno":"20b-017-se"},
    2:{"name":"aun","rollno":"20b-118-se"},
    3:{"name":"farhan","rollno":"20b-055-se"}
}

def notFound(studen_id):
    if studen_id not in students:
        abort(404,message="Student not found")

class Student(Resource):
    def get(self,id):
        notFound(id)
        return students[id]

    def put(self,id):
        newStd = student_put.parse_args()
        students[id] = newStd
        return students[id]

    def post(self,id):
        newStd = student_put.parse_args()
        newid = int(max(students.keys()))+1
        students[newid] = newStd
        print(students)
        return students[newid]

    def delete(self,id):
        del students[id]

API.add_resource(Student,"/show/<int:id>")

if __name__=="__main__":
    app.run(debug=True)