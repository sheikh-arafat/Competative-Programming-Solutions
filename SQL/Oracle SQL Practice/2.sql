/*
2. Show the top 3 departments where most employees work
Ans:
*/
SELECT d.department_name, d.department_id, COUNT(e.employee_id) AS Total_Employee
FROM hr.departments d
INNER JOIN hr.employees e
ON d.department_id = e.department_id
GROUP BY d.department_name, d.department_id
ORDER BY Total_Employee DESC
FETCH FIRST 3 ROWS ONLY;

/*
Another Ans:
*/
SELECT *
FROM(
    SELECT d.department_name, d.department_id, COUNT(e.employee_id) AS Total_Employee
    FROM hr.departments d
    INNER JOIN hr.employees e
    ON d.department_id = e.department_id
    GROUP BY d.department_name, d.department_id
    ORDER BY Total_Employee DESC
)
WHERE ROWNUM <= 3;
