
def test_get_students_should_return_empty_list_if_no_student_has_been_created(client):
    response = client.get("/students")
    # assert response.status_code == 200
    # assert response.json == []

# def tests_get_students_should_return_all_created_users(client):
# def get_studentss?specialization=Math
# def get_students?name=Bob
# def get_students?name...&specialization...

# get_student - 200
# get_student - 404

# def create_student - 201
# def create_student - 400/422

# def update_student - 200
# def update_student - 404
# def update_student - 400/422

# def delete_student - 200 (nawet jeśli nie było obiektu)
# def delete_student - 200 / i obiekt usunięty
