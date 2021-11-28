import uuid

from sqlalchemy.dialects.postgresql import UUID

from students_manager import db


class Student(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)

    def __init__(self, name, surname, specialization):
        self.name = name
        self.surname = surname
        self.specialization = specialization
