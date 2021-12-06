import json
import uuid
import factory

from tests.factories import StudentFactory


def test_get_students_with_no_entity_should_return_empty_list(client):
    # Act
    response = client.get("/students")
    # Assert
    assert [] == response.json


def test_get_student_with_entity_should_return_entities_list(client):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)
    client.post("/students", data=json.dumps(student), content_type="application/json")

    # Act
    response = client.get("/students")

    # Assert
    assert student["name"] in [student["name"] for student in response.json]


def test_get_student_with_non_existing_entity_should_return_404(client):
    # Act
    response = client.get(f"/students/{uuid.uuid4()}")

    # Assert
    assert response.status_code == 404


def test_get_studenrt_with_existing_student_should_return_entity(client):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)
    created_student = client.post(
        "/students", data=json.dumps(student), content_type="application/json"
    ).json["id"]

    # Act
    response = client.get(f"/students/{created_student}")

    # Assert
    assert response.json["name"] == student["name"]
    assert response.json["surname"] == student["surname"]
    assert response.json["specialization"] == student["specialization"]


def test_create_student_should_return_201_and_created_entity(client):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)

    # Act
    response = client.post(
        "/students", data=json.dumps(student), content_type="application/json"
    )

    # Assert
    assert response.status_code == 201
    assert response.json["name"] == student["name"]
    assert response.json["surname"] == student["surname"]
    assert response.json["specialization"] == student["specialization"]


def test_delete_student_with_existing_student_should_return_entity(client):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)
    created_student = client.post(
        "/students", data=json.dumps(student), content_type="application/json"
    ).json["id"]

    # Act
    client.delete(f"/students/{created_student}")
    response = client.get(f"/students/{created_student}")

    # Assert
    assert response.status_code == 404
