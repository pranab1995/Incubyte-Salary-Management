# Planning Notes

## Assessment Understanding

Build a minimal yet usable salary management tool for an HR manager.

The product should support:

- Managing employee records from the UI.
- Viewing salary insights from the UI.
- Seeding 10,000 employees efficiently from first and last name source files.
- A backend, frontend, database, tests, and deployment/readiness notes.

## User Persona

The primary user is an HR manager. They need to maintain employee compensation data and quickly inspect salary patterns by country and role.

This means the UI should be practical and information-dense rather than decorative.

## Initial Domain

Employee fields planned for the first version:

- Full name
- Job title
- Country
- Salary
- Department
- Employment type
- Hire date
- Email

## TDD Roadmap

1. Add failing tests for employee creation through the API.
2. Implement the smallest Django/DRF model and endpoint to pass creation.
3. Add failing tests for update and delete.
4. Implement update and delete.
5. Add failing tests for salary insights.
6. Implement country and job-title salary aggregation.
7. Add failing tests for deterministic seed generation.
8. Implement the seed generator and management command.
9. Add frontend tests for salary formatting and form behavior.
10. Build the Angular UI against the working API.

## AI Usage Intent

AI will be used as a collaborator for planning, scaffolding suggestions, test ideas, and review. The implementation will be reviewed and committed in small slices so the evolution remains understandable.

## Environment Choice

Pipenv is used for backend dependency management because it keeps runtime and development dependencies explicit in a workflow I am comfortable maintaining.
