import random
from django.core.management.base import BaseCommand
from django.db import transaction
from employees.models import Employee
from faker import Faker

class Command(BaseCommand):
    help = 'Seeds the database with employee data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10000, help='Number of employees to create')

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()
        
        self.stdout.write(self.style.WARNING(f'Deleting all existing employees...'))
        Employee.objects.all().delete()
        
        departments = ["Engineering", "Sales", "Marketing", "HR", "Finance", "Product"]
        job_titles = ["Software Engineer", "Senior Software Engineer", "Product Manager", "HR Generalist", "Sales Executive", "Marketing Manager"]
        countries = ["USA", "India", "UK", "Canada", "Germany", "Australia"]
        
        self.stdout.write(self.style.SUCCESS(f'Generating {count} employees...'))
        
        batch_size = 5000
        employees = []
        
        with transaction.atomic():
            for i in range(count):
                emp = Employee(
                    full_name=fake.name(),
                    job_title=random.choice(job_titles),
                    country=random.choice(countries),
                    salary=round(random.uniform(30000, 200000), 2),
                    department=random.choice(departments),
                    employment_type=random.choice([e[0] for e in Employee.EmploymentType.choices]),
                    hire_date=fake.date_between(start_date='-5y', end_date='today'),
                    email=fake.unique.email()
                )
                employees.append(emp)
                
                if len(employees) >= batch_size:
                    Employee.objects.bulk_create(employees)
                    self.stdout.write(f'Created {i+1} employees...')
                    employees = []
            
            if employees:
                Employee.objects.bulk_create(employees)
                
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {count} employees.'))
