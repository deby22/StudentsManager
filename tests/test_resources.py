import json
import uuid

import factory

from tests.factories import StudentFactory


def test_get_students_with_no_entity_should_return_empty_list(client):
    # Act
    response = client.get("/students/")
    # Assert
    assert [] == response.json


def test_get_student_with_entity_should_return_entities_list(client):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)
    client.post("/students/", data=json.dumps(student), content_type="application/json")

    # Act
    response = client.get("/students/")

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
        "/students/", data=json.dumps(student), content_type="application/json"
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
        "/students/", data=json.dumps(student), content_type="application/json"
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
        "/students/", data=json.dumps(student), content_type="application/json"
    ).json["id"]

    # Act
    client.delete(f"/students/{created_student}")
    response = client.get(f"/students/{created_student}")

    # Assert
    assert response.status_code == 404


def test_delete_should_return_200_on_non_existing_entity(client):
    response = client.delete(f"/students/{uuid.uuid4()}")
    assert response.status_code == 200


def test_delete_should_return_200_on_existing_entity(client):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)
    created_student = client.post(
        "/students/", data=json.dumps(student), content_type="application/json"
    ).json["id"]

    # Act
    response = client.delete(f"/students/{created_student}")

    # arrange
    assert response.status_code == 200


def test_update_student_with_existing_student_and_empty_json_data_should_not_update_entity(
    client,
):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)
    created_student = client.post(
        "/students/", data=json.dumps(student), content_type="application/json"
    ).json["id"]

    # Act
    response = client.put(
        f"/students/{created_student}",
        data=json.dumps({}),
        content_type="application/json",
    )

    # Assert
    assert response.status_code == 200
    assert response.json["name"] == student["name"]
    assert response.json["surname"] == student["surname"]
    assert response.json["specialization"] == student["specialization"]


def test_update_student_with_existing_student_and_non_empty_json_data_should_not_update_entity(
    client,
):
    # Arrange
    student = factory.build(dict, FACTORY_CLASS=StudentFactory)
    created_student = client.post(
        "/students/", data=json.dumps(student), content_type="application/json"
    ).json["id"]
    updated_student = {
        "name": "New name",
        "surname": "New surname",
        "specialization": "New specialization",
    }

    # Act
    response = client.put(
        f"/students/{created_student}",
        data=json.dumps(updated_student),
        content_type="application/json",
    )

    # Assert
    assert response.status_code == 200
    assert response.json["name"] == updated_student["name"]
    assert response.json["surname"] == updated_student["surname"]
    assert response.json["specialization"] == updated_student["specialization"]


def test_update_student_with_non_existing_student_should_not_update_entity(client):
    # Act
    response = client.get(f"/students/{uuid.uuid4()}")

    # Assert
    assert response.status_code == 404
