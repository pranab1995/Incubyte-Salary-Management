# TDD Log

This log records the main red-green-refactor slices used during the assessment.

## 1. Planning

Before writing production code, I captured the product scope, user persona, stack choice, and intended TDD roadmap.

## 2. Employee Creation API

Red: Added a DRF API test that describes how an HR manager creates an employee with the required salary management fields.

Green: Added the initial Django project, employee model, serializer, router, and migration needed to create employees through the API.

## 3. Employee Management API

Red: Added tests for viewing the employee list, updating salary, and deleting an employee.

Green: The existing DRF `ModelViewSet` already supported these flows, so no production code was needed. The tests now lock the expected behavior in place.

## 4. Salary Insights API

Red: Added tests for country-level salary summary and job-title average salary within a country.

Green: Implemented a salary insights endpoint backed by Django ORM aggregate queries.

## 5. Frontend Salary Formatting

Red: Added an Angular unit test for salary display formatting.

Green: Added the first Angular UI slice with employee creation, employee list display, and salary insights.
