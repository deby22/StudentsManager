from flask import Blueprint, request
from flask.json import jsonify

from .models import Student
from .schemas import StudentSchema

from students_manager import db

students = Blueprint("students", __name__)


@students.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    schema = StudentSchema(many=True)
    return jsonify(schema.dump(students))


@students.route("/students", methods=["POST"])
def create_students():
    name = request.json["name"]
    surname = request.json["surname"]
    specialization = request.json["specialization"]
    student = Student(name=name, surname=surname, specialization=specialization)
    db.session.add(student)
    db.session.commit()
    schema = StudentSchema()
    return schema.dump(student), 201


@students.route("/students/<string:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    schema = StudentSchema()
    return schema.dump(student)


@students.route("/students/<string:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    if name := request.json.get("name"):
        student.name = name
    if surname := request.json.get("surname"):
        student.surname = surname
    if specialization := request.json.get("specialization"):
        student.specialization = specialization
    db.session.add(student)
    db.session.commit()

    schema = StudentSchema()
    return schema.dump(student)


@students.route("/students/<string:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    schema = StudentSchema()
    return schema.dump(student)
