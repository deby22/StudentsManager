from students_manager import ma


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "surname", "specialization")
