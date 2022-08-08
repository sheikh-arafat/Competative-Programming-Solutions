/*
5. Display manager information and how many subordinates they manage (count)
Partial Ans:
*/
SELECT DISTINCT d.department_id, COUNT(e.employee_id) - 1 AS Subordinates, d.manager_id
FROM hr.departments d
INNER JOIN hr.employees e
ON d.department_id = e.department_id
GROUP BY d.department_id, d.manager_id;
