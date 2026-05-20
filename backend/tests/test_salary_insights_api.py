from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from employees.models import Employee


pytestmark = pytest.mark.django_db


def create_employee(
    *,
    full_name,
    job_title,
    country,
    salary,
    department="Engineering",
    email,
):
    return Employee.objects.create(
        full_name=full_name,
        job_title=job_title,
        country=country,
        salary=salary,
        department=department,
        employment_type=Employee.EmploymentType.FULL_TIME,
        hire_date="2023-01-01",
        email=email,
    )


def test_country_salary_summary_includes_min_max_average_and_count():
    create_employee(
        full_name="Aarav Patel",
        job_title="Software Engineer",
        country="India",
        salary=Decimal("1200000.00"),
        email="aarav.patel@example.com",
    )
    create_employee(
        full_name="Isha Rao",
        job_title="Senior Software Engineer",
        country="India",
        salary=Decimal("2400000.00"),
        email="isha.rao@example.com",
    )
    create_employee(
        full_name="Noah Smith",
        job_title="Software Engineer",
        country="United States",
        salary=Decimal("120000.00"),
        email="noah.smith@example.com",
    )

    response = APIClient().get(reverse("salary-insights"), {"country": "India"})

    assert response.status_code == status.HTTP_200_OK
    assert response.data["country"] == "India"
    assert response.data["employee_count"] == 2
    assert Decimal(response.data["minimum_salary"]) == Decimal("1200000.00")
    assert Decimal(response.data["maximum_salary"]) == Decimal("2400000.00")
    assert Decimal(response.data["average_salary"]) == Decimal("1800000.00")


def test_country_job_title_average_salary_is_available():
    create_employee(
        full_name="Dev Malhotra",
        job_title="Data Scientist",
        country="India",
        salary=Decimal("2000000.00"),
        email="dev.malhotra@example.com",
    )
    create_employee(
        full_name="Sara Thomas",
        job_title="Data Scientist",
        country="India",
        salary=Decimal("2600000.00"),
        email="sara.thomas@example.com",
    )
    create_employee(
        full_name="Liam Brown",
        job_title="Data Scientist",
        country="United Kingdom",
        salary=Decimal("90000.00"),
        email="liam.brown@example.com",
    )

    response = APIClient().get(
        reverse("salary-insights"),
        {"country": "India", "job_title": "Data Scientist"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert Decimal(response.data["job_title_average_salary"]) == Decimal("2300000.00")
