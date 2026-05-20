from django.urls import include, path
from rest_framework.routers import DefaultRouter

from employees.api import salary_insights
from employees.views import EmployeeViewSet


router = DefaultRouter()
router.register("employees", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/salary-insights/", salary_insights, name="salary-insights"),
]
