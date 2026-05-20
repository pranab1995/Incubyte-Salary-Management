from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db


def test_hr_manager_can_create_employee():
    client = APIClient()
    payload = {
        "full_name": "Ananya Sharma",
        "job_title": "Senior Software Engineer",
        "country": "India",
        "salary": "3200000.00",
        "department": "Engineering",
        "employment_type": "FULL_TIME",
        "hire_date": "2023-04-10",
        "email": "ananya.sharma@example.com",
    }

    response = client.post(reverse("employee-list"), payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["full_name"] == "Ananya Sharma"
    assert response.data["country"] == "India"
    assert Decimal(response.data["salary"]) == Decimal("3200000.00")
