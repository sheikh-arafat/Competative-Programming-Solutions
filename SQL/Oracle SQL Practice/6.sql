/*6. Which month and year the company hired the most employees? [from 01-Jan-1995 to 31-DEC-2005]
Ans:
*/

select to_char(hire_date,'YYYY') Year, to_char(hire_date,'MON') Month, 
count (employee_id) "no of employees" 
from hr.employees 
where hire_date >= '01-Jan-1995' and hire_date<= '31-DEC-2005'  
group by to_char(hire_date,'YYYY'),to_char(hire_date,'MON') 
order by "no of employees" desc 
fetch first row with ties;
