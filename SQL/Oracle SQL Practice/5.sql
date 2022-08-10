/*
5. Display manager information and how many subordinates they manage (count)
Ans:
*/
select m.employee_id, m.first_name, m.last_name , count(e.employee_id) subordinates 
from hr.employees e 
join hr.employees m 
on e.manager_id =  m.employee_id 
group by m.employee_id,m.first_name, m.last_name 
order by m.employee_id;
