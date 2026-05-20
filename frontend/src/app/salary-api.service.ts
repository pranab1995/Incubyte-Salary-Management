import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import {
  Employee,
  EmployeePayload,
  PaginatedEmployees,
  SalaryInsights,
} from './api.types';

@Injectable({ providedIn: 'root' })
export class SalaryApiService {
  constructor(private readonly http: HttpClient) {}

  listEmployees(): Observable<PaginatedEmployees> {
    return this.http.get<PaginatedEmployees>('/api/employees/');
  }

  createEmployee(payload: EmployeePayload): Observable<Employee> {
    return this.http.post<Employee>('/api/employees/', payload);
  }

  getSalaryInsights(country: string, jobTitle = ''): Observable<SalaryInsights> {
    let params = new HttpParams().set('country', country);
    if (jobTitle) {
      params = params.set('job_title', jobTitle);
    }

    return this.http.get<SalaryInsights>('/api/salary-insights/', { params });
  }
}
