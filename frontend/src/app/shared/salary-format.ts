export function formatSalary(value: string | number | null | undefined): string {
  if (value === null || value === undefined || value === '') {
    return 'Not available';
  }

  return Number(value).toLocaleString('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
}
