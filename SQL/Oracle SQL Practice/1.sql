/*1. Show the employees who get the highest salary in each department
Ans:
*/

SELECT first_name, last_name, Salary
FROM hr.employees
WHERE (department_id,Salary) IN(
    SELECT department_id, MAX(salary)
    FROM hr.employees
    GROUP BY department_id
)
ORDER BY salary DESC;
