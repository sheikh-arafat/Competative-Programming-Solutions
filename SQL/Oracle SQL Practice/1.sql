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
