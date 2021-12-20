from flask.json import jsonify
from flask_restx import Namespace, Resource

from students_manager.common import Repo

from .api import api
from .service import StudentService

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
        result = StudentService().all()
        return result.result, result.status_code

    @student_namespace.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        result = StudentService().create(args)
        return result.result, result.status_code


@student_namespace.route("/<string:id>")
@student_namespace.response(404, "Student not found")
@student_namespace.param("id", "The student identifier")
class StudentDetailResource(Resource):
    def get(self, id: int):
        result = StudentService().get(id)
        return result.result, result.status_code

    def delete(self, id: str):
        result = StudentService().delete(id)
        return result.result, result.status_code

    @student_namespace.doc(parser=parser)
    def put(self, id: str):
        args = parser.parse_args()
        result = StudentService().update(id, args)
        return result.result, result.status_code
