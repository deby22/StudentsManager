from flask.json import jsonify
from flask_restx import Namespace, Resource
from students_manager.common import Repo

from .api import api
from .models import Student
from .schemas import StudentSchema

parser = api.parser()
parser.add_argument(
    "name",
    type=str,
    required=False,
    help="Student name",
)
parser.add_argument(
    "surname",
    type=str,
    required=False,
    help="Student surname",
)
parser.add_argument(
    "specialization",
    type=str,
    required=False,
    help="Student specialization",
)

student_namespace = Namespace("students", description="Students namespace")


@student_namespace.route("/")
class StudentListResource(Resource):
    def get(self):
        students = Repo.all(Student)
        schema = StudentSchema(many=True)
        return jsonify(schema.dump(students))

    @student_namespace.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        name = args.get("name")
        surname = args.get("surname")
        specialization = args.get("specialization")
        student = Student(name=name, surname=surname, specialization=specialization)
        Repo.save(student)
        schema = StudentSchema()
        return schema.dump(student), 201


@student_namespace.route("/<string:id>")
@student_namespace.response(404, "Student not found")
@student_namespace.param("id", "The student identifier")
class StudentDetailResource(Resource):
    def get(self, id: int):
        if student := Repo.get(Student, id):
            schema = StudentSchema()
            return schema.dump(student), 200
        else:
            return {}, 404

    def delete(self, id: str):
        Repo.delete(Student, id)
        return {}, 200

    @student_namespace.doc(parser=parser)
    def put(self, id: str):
        args = parser.parse_args()
        student = Student.query.get_or_404(id)
        if name := args.get("name"):
            student.name = name
        if surname := args.get("surname"):
            student.surname = surname
        if specialization := args.get("specialization"):
            student.specialization = specialization
        Repo.save(student)
        schema = StudentSchema()
        return schema.dump(student)
