from students_manager.common import (BAD_REQUEST, CREATED, NOT_FOUND, OK, Repo,
                                     Result)
from students_manager.students.models import Student
from students_manager.students.schemas import StudentSchema


class StudentService:
    def __init__(self, repo=Repo):
        self.repo = repo()

    def all(self):
        students = self.repo.all(Student)
        schema = StudentSchema(many=True)
        return Result(is_successful=True, result=schema.dump(students), status_code=OK)

    def get(self, id: str):
        if student := self.repo.get(Student, id):
            schema = StudentSchema()
            return Result(
                is_successful=True, result=schema.dump(student), status_code=CREATED
            )
        else:
            return Result(
                is_successful=False,
                result=["Object does not exist"],
                status_code=NOT_FOUND,
            )

    def delete(self, id: str):
        self.repo.delete(Student, id)
        return Result(is_successful=True, status_code=OK)

    def create(self, args: dict):
        name = args.get("name")
        surname = args.get("surname")
        specialization = args.get("specialization")
        student = Student(name=name, surname=surname, specialization=specialization)
        self.repo.save(student)
        schema = StudentSchema()
        return Result(
            is_successful=True, result=schema.dump(student), status_code=CREATED
        )

    def update(self, id: str, args: dict):
        student = self.repo.get(Student, id)
        if not student:
            return Result(
                is_successful=False,
                result=["Object does not exist"],
                status_code=NOT_FOUND,
            )
        else:
            if name := args.get("name"):
                student.name = name
            if surname := args.get("surname"):
                student.surname = surname
            if specialization := args.get("specialization"):
                student.specialization = specialization
            self.repo.save(student)
            schema = StudentSchema()
            return Result(
                is_successful=True, result=schema.dump(student), status_code=OK
            )
