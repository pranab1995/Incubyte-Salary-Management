from rest_framework.viewsets import ModelViewSet

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ["country", "department", "job_title", "employment_type"]
    search_fields = ["full_name", "email", "job_title"]
    ordering_fields = ["full_name", "salary", "hire_date", "created_at"]
    ordering = ["full_name"]
