/*
8. Display details of manager who manages another manager [hierarchical]
Ans:
*/

select distinct m.employee_id,m.first_name, m.last_name 
from hr.employees e join hr.employees m 
on e.manager_id =  m.employee_id 
where e.employee_id 
in( select distinct manager_id from hr.employees) 
order by m.employee_id;
