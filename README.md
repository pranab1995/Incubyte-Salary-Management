# Incubyte Salary Management

Salary management assessment for Incubyte's Software Craftsperson/Python/AI-III role.

This repository will be built incrementally using TDD. The goal is to create a minimal but usable salary management tool for an HR manager responsible for an organization of 10,000 employees.

## Planned Stack

- Backend: Django and Django REST Framework
- Database: SQLite for simple local review, with Django ORM portability for MySQL
- Frontend: Angular
- Tests: Django/DRF tests first, Angular tests for UI logic where useful

## Assessment Goals

- End-to-end working salary management software
- Employee add, view, update, and delete flows
- Salary insights by country and job title
- Deterministic seed script for 10,000 employees
- Small commits that show the solution evolving through TDD
- Notes on architecture, trade-offs, performance, and AI usage

## Backend Setup

```bash
cd backend
pipenv install --dev
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

Run backend tests:

```bash
cd backend
pipenv run pytest
```

The API is mounted under `http://localhost:8000/api/`.
