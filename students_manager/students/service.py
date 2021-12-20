from students_manager.common import Result

from students_manager.common import Repo
from students_manager.students.models import Student
from students_manager.students.schemas import StudentSchema
from students_manager.common import Result


class StudentService:
    def get(self, id: str):
        student = Student.query.get(id)
        if student:
            schema = StudentSchema()
            return Result(is_successful=True, result=schema.dump(student))
        else:
            return Result(is_successful=False, errors=["Object does not exist"])

    def delete(self, id: str):
        student = Student.query.get(id)
        if student:
            db.session.delete(student)
            db.session.commit()
            schema = StudentSchema()
            return schema.dump(student), 200
        return {}, 200
