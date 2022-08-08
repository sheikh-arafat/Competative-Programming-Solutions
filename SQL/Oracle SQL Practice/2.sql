/*
2. Show the top 3 departments where most employees work
Partial Ans:
select distinct m.* from hr.employees e ,  hr.employees m where m.employee_id = e.manager_id;

Ans:
*/
SELECT DISTINCT e.*, m.department_name
FROM hr.employees e
INNER JOIN hr.departments m
ON e.department_id = m.department_id
WHERE m.manager_id = e.employee_id;
