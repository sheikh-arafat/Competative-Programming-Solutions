/*1A. Show the highest salary in each department
Ans:
*/
select dep.department_name, max(salary)
from hr.employees emp
inner join hr.departments dep
on dep.department_id = emp.department_id
group by dep.department_name
order by max(salary) desc;
