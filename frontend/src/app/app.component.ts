import { CommonModule } from '@angular/common';
import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { Employee, EmployeePayload, SalaryInsights } from './api.types';
import { SalaryApiService } from './salary-api.service';
import { formatSalary } from './shared/salary-format';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit {
  private readonly api = inject(SalaryApiService);
  private readonly fb = inject(FormBuilder);

  employees: Employee[] = [];
  totalEmployees = 0;
  insights: SalaryInsights | null = null;
  feedback = '';

  readonly employeeForm = this.fb.nonNullable.group({
    full_name: ['', [Validators.required]],
    job_title: ['', [Validators.required]],
    country: ['India', [Validators.required]],
    salary: ['1200000.00', [Validators.required]],
    department: ['Engineering', [Validators.required]],
    employment_type: ['FULL_TIME' as EmployeePayload['employment_type'], [Validators.required]],
    hire_date: ['2024-01-01', [Validators.required]],
    email: ['', [Validators.required, Validators.email]],
  });

  readonly insightsForm = this.fb.nonNullable.group({
    country: ['India', [Validators.required]],
    job_title: [''],
  });

  ngOnInit(): void {
    this.loadEmployees();
    this.loadInsights();
  }

  loadEmployees(): void {
    this.api.listEmployees().subscribe({
      next: (page) => {
        this.employees = page.results;
        this.totalEmployees = page.count;
      },
      error: () => (this.feedback = 'Unable to load employees.'),
    });
  }

  addEmployee(): void {
    if (this.employeeForm.invalid) {
      this.employeeForm.markAllAsTouched();
      return;
    }

    this.api.createEmployee(this.employeeForm.getRawValue()).subscribe({
      next: () => {
        this.feedback = 'Employee added.';
        this.employeeForm.patchValue({ full_name: '', email: '' });
        this.loadEmployees();
        this.loadInsights();
      },
      error: () => (this.feedback = 'Unable to add employee. Check required fields and unique email.'),
    });
  }

  loadInsights(): void {
    const query = this.insightsForm.getRawValue();
    this.api.getSalaryInsights(query.country, query.job_title).subscribe({
      next: (insights) => (this.insights = insights),
      error: () => (this.feedback = 'Unable to load salary insights.'),
    });
  }

  formatSalary(value: string | null | undefined): string {
    return formatSalary(value);
  }
}
