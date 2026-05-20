from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def employee_payload(**overrides):
    payload = {
        "full_name": "Rohan Mehta",
        "job_title": "Product Manager",
        "country": "India",
        "salary": "2800000.00",
        "department": "Product",
        "employment_type": "FULL_TIME",
        "hire_date": "2022-08-01",
        "email": "rohan.mehta@example.com",
    }
    payload.update(overrides)
    return payload


def create_employee(client, **overrides):
    response = client.post(reverse("employee-list"), employee_payload(**overrides), format="json")
    assert response.status_code == status.HTTP_201_CREATED
    return response.data


def test_hr_manager_can_view_employee_list():
    client = APIClient()
    create_employee(client, full_name="Ananya Sharma", email="ananya.list@example.com")
    create_employee(client, full_name="Maya Nair", email="maya.list@example.com")

    response = client.get(reverse("employee-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 2
    assert {employee["full_name"] for employee in response.data["results"]} == {
        "Ananya Sharma",
        "Maya Nair",
    }


def test_hr_manager_can_update_employee_salary():
    client = APIClient()
    employee = create_employee(client)
    employee_url = reverse("employee-detail", args=[employee["id"]])

    response = client.patch(employee_url, {"salary": "3000000.00"}, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert Decimal(response.data["salary"]) == Decimal("3000000.00")


def test_hr_manager_can_delete_employee():
    client = APIClient()
    employee = create_employee(client)
    employee_url = reverse("employee-detail", args=[employee["id"]])

    response = client.delete(employee_url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert client.get(employee_url).status_code == status.HTTP_404_NOT_FOUND
