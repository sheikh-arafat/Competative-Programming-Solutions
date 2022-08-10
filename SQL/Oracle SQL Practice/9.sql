/*
9. Display if an employee’s salary is higher, lower or equal to the previous employee
Ans:
*/

SELECT e.*,
LAG(salary) OVER(PARTITION BY department_id ORDER BY employee_id) AS previous_emp_salary,
CASE WHEN e.salary > LAG(salary) OVER(PARTITION BY department_id ORDER BY employee_id) THEN 'Higher than previous employee'
     WHEN e.salary < LAG(salary) OVER(PARTITION BY department_id ORDER BY employee_id) THEN 'Lower than previous employee'
     WHEN e.salary = LAG(salary) OVER(PARTITION BY department_id ORDER BY employee_id) THEN 'Same as previous employee'
END sal_range
FROM hr.employees e;
