from django.db.models import Avg, Count, Max, Min

from employees.models import Employee


def salary_summary_for_country(country, job_title=None):
    employees_in_country = Employee.objects.filter(country=country)
    summary = employees_in_country.aggregate(
        employee_count=Count("id"),
        minimum_salary=Min("salary"),
        maximum_salary=Max("salary"),
        average_salary=Avg("salary"),
    )

    data = {
        "country": country,
        "employee_count": summary["employee_count"],
        "minimum_salary": summary["minimum_salary"],
        "maximum_salary": summary["maximum_salary"],
        "average_salary": summary["average_salary"],
    }

    if job_title:
        data["job_title"] = job_title
        data["job_title_average_salary"] = employees_in_country.filter(
            job_title=job_title
        ).aggregate(average_salary=Avg("salary"))["average_salary"]

    return data
