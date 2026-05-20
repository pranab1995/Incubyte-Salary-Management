import { formatSalary } from './salary-format';

describe('formatSalary', () => {
  it('formats salary with two decimals and readable separators', () => {
    expect(formatSalary('3200000.00')).toBe('3,200,000.00');
  });

  it('shows unavailable when salary is missing', () => {
    expect(formatSalary(null)).toBe('Not available');
  });
});
