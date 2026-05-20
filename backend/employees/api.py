from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employees.insights import salary_summary_for_country


class SalaryInsightsQuerySerializer(serializers.Serializer):
    country = serializers.CharField(max_length=80)
    job_title = serializers.CharField(max_length=100, required=False)


class SalaryInsightsSerializer(serializers.Serializer):
    country = serializers.CharField()
    employee_count = serializers.IntegerField()
    minimum_salary = serializers.DecimalField(max_digits=12, decimal_places=2, allow_null=True)
    maximum_salary = serializers.DecimalField(max_digits=12, decimal_places=2, allow_null=True)
    average_salary = serializers.DecimalField(max_digits=12, decimal_places=2, allow_null=True)
    job_title = serializers.CharField(required=False)
    job_title_average_salary = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        allow_null=True,
        required=False,
    )


@api_view(["GET"])
def salary_insights(request):
    query_serializer = SalaryInsightsQuerySerializer(data=request.query_params)
    query_serializer.is_valid(raise_exception=True)

    summary = salary_summary_for_country(**query_serializer.validated_data)
    serializer = SalaryInsightsSerializer(summary)
    return Response(serializer.data, status=status.HTTP_200_OK)
