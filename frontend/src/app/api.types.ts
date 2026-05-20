export type EmploymentType = 'FULL_TIME' | 'PART_TIME' | 'CONTRACT' | 'INTERN';

export interface Employee {
  id: number;
  full_name: string;
  job_title: string;
  country: string;
  salary: string;
  department: string;
  employment_type: EmploymentType;
  hire_date: string;
  email: string;
}

export interface EmployeePayload {
  full_name: string;
  job_title: string;
  country: string;
  salary: string;
  department: string;
  employment_type: EmploymentType;
  hire_date: string;
  email: string;
}

export interface PaginatedEmployees {
  count: number;
  next: string | null;
  previous: string | null;
  results: Employee[];
}

export interface SalaryInsights {
  country: string;
  employee_count: number;
  minimum_salary: string | null;
  maximum_salary: string | null;
  average_salary: string | null;
  job_title_average_salary?: string | null;
}
