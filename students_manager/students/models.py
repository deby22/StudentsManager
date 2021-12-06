import uuid

from sqlalchemy.dialects.postgresql import UUID

from students_manager import db


class Student(db.Model):
    # id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = db.Column(
        db.String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True
    )
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)


# Notes
# instead of UUID fields i use db.String becouse sqlite doesn't support UUID field
# its much easier to use sqlite in test
