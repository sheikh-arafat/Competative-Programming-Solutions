/*
7. Display the month in which more than 3 employees joined and in which department
Partial Ans:
*/
select to_char(hire_date,'MON') Month, count(employee_id) "no of employees" 
from hr.employees 
where hire_date >= '01-Jan-1995' and hire_date<= '31-DEC-2005'
having count(employee_id) >3
group by to_char(hire_date,'MON') 
order by "no of employees" desc ;
