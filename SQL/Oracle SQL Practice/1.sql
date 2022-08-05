/*1. Show the employees who get the highest salary in each department
Ans:
*/

select first_name, last_name
from hr.employees
where salary in(
    select max(salary)
    from hr.employees
    group by department_id
);

/* Ans 2 */

SELECT 
    first_name
    , Salary
    , department_id 
FROM hr.employees 
WHERE
     (department_id,Salary) 
     in 
     (select department_id, max(salary) from hr.employees group by department_id)
     ORDER BY salary desc;
