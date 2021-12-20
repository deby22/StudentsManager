from students_manager.students.api import api
from students_manager.students.resources import student_namespace


api.add_namespace(student_namespace)
