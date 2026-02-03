# Write your MySQL query statement below
select e.employee_id, e.name, count(m.employee_id) as reports_count, ceiling(avg(m.age)) as average_age 
from Employees e
join Employees m on e.employee_id = m.reports_to
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id